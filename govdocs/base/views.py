import random
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Document, UserPoints, InputLog
from django.contrib.auth.models import User
import base64
from PyPDF2 import PdfReader
from pdf2image import convert_from_path
import tempfile
from django.contrib import messages
from .forms import InputLogForm


# Create your views here.
def home(request):
    context = {
        'user': request.user,  # Passando o objeto user diretamente para o template
    }
    return render(request, 'base/home.html', context)

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")
        
        user = authenticate(request, username=username, password=password) 
        if user:
            login(request, user) 
            return redirect('home')
        else:
            messages.error(request, "Username or password does not exist")

        
    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) 
            user.username = user.username.lower()
            user.save()
            login(request, user) 
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
            
    return render(request, 'base/login_register.html', {'form': form}) 

def userProfile(request, pk):
    user = get_object_or_404(User, id=pk)
    user_points, created = UserPoints.objects.get_or_create(user=user, defaults={'points': 0})
    '''
    Tente obter a pontuação para o user especificado.
    Se essa pontuação não existir, crie uma nova pontuação para esse user com points inicializados em 0.
    Atribua o objeto encontrado ou criado a user_points.
    Atribua True a created se um novo objeto foi criado, ou False se o objeto já existia e foi apenas recuperado.
    '''
    context = {
        'user': user,
        'points': user_points.points  # Adiciona os pontos ao contexto
    }
    return render(request, 'base/profile.html', context)

# def add_title_date_feedback(request, doc_id):
#     if request.method == 'POST':
#         form = InputLogForm(request.POST)
#         if form.is_valid():
#             input_log = form.save(commit=False)
#             # Defina 'user_id' como o usuário atualmente logado.
#             input_log.user_id = User.objects.get(id=request.user.id)
#             # Defina 'doc_id' conforme necessário, aqui é apenas um exemplo.
#             input_log.doc_id = get_object_or_404(Document, pk=doc_id)
#             input_log.save()
#             return redirect('home')
#         else:
#             form = InputLogForm()

#         context = {
#         'form': form,
#         'doc_id': doc_id,
#     }
        
#     return render(request, 'base/title_date_feedback.html')
    

    
# Random para gerar um numero aleatorio de 0 ate o tamanho do banco
# Pega o doc_id, com isso pega o doc_type e para cada doctype(AUDIOVISUAL: mp4;CARTOGRAFICO: pdf ;ICONOGRAFICO: pdf ;SONORO:mp3 ;TEXTUAL: pdf ) e trata diferente para cada.
'''
def show_doc(request, doc_id):
    doc_id = 'BR_RJANRIO_04_0_MAP_00570_d0001de0001'
    table_length = Document.objects.count()
    random_id = random.randint(0,table_length)
    random_document = Document.objects.get(doc_id=random_id)
    doc_type = random_document.doc_type
    print("\n\n\nTESTE")
    print(doc_type)
    print("TESTE\n\n\n")
    if random_document.doc_type:
        doc_type_mapping = {
            0: "mp4",
            1: "pdf",
            2: "pdf",
            3: "mp3",
            4: "pdf"
        }
    if doc_type in doc_type_mapping:
       document_type = doc_type_mapping[doc_type] 
    return render(request, 'base/home.html', {'document': random_document, 'type': document_type})
'''

#WORKED
# def show_doc(request, doc_id, page_number=1):
#     document = get_object_or_404(Document, doc_id=doc_id)
#     # Open the PDF file
#     pdf_content = document.doc.open('rb')
    
#     # Convert PDF to images (each page becomes an image)
#     images = convert_from_path(pdf_content.name, dpi=50, first_page=page_number, last_page=page_number, poppler_path=r'C:\Program Files (x86)\Release-24.02.0-0\poppler-24.02.0\Library\bin')
    
#     image_data = []
#     for image in images:
#         with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp:
#             image.save(temp.name, 'PNG')
#             temp.seek(0)
#             encoded_string = base64.b64encode(temp.read()).decode('utf-8')
#             image_data.append(encoded_string)

#     return render(request, 'base/pdf_viewer.html', {
#         'image_data': image_data,
#         'doc_id': doc_id,
#         'current_page': page_number
#     })
    


def show_doc(request, doc_id=None, page_number=1, randomize=0):
    if randomize:
        # Retrieve a random document that is not audiovisual (0) or sonoro (3)
        documents_length = Document.objects.count()
        while True:
            random_index = random.randint(0, documents_length - 1)
            document = Document.objects.all()[random_index]
            if document.doc_type not in [0, 3]:
                doc_id = document.doc_id
                break
        # Redirect to the document-specific URL with the first page
        return redirect('show-doc-page', doc_id=doc_id, page_number=1)
    else:
        # Retrieve the specified document
        document = get_object_or_404(Document, doc_id=doc_id)

    pdf_path = document.doc.path
    pdf = PdfReader(pdf_path)
    page = pdf.pages[page_number-1]
    media_box = page.mediabox

    # Calculate height in inches
    height_in_inches = (media_box[3] - media_box[1]) / 72  # PDF units are points, 1 point = 1/72 inches

    # Calculate required DPI to achieve 400px height
    target_pixel_height = 400
    dpi = int(target_pixel_height / height_in_inches)

    # Convert the specified PDF page to an image at calculated DPI
    images = convert_from_path(pdf_path, first_page=page_number, last_page=page_number, dpi=dpi, poppler_path=r'C:\Program Files (x86)\Release-24.02.0-0\poppler-24.02.0\Library\bin')

    image_data = []
    for image in images:
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp:
            image.save(temp.name, 'PNG')
            temp.seek(0)
            encoded_string = base64.b64encode(temp.read()).decode('utf-8')
            image_data.append(encoded_string)

    return render(request, 'base/home.html', {
        'image_data': image_data,
        'total_pages': len(pdf.pages),
        'doc_id': doc_id,
        'current_page': page_number
    })