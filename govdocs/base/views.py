import random
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Document
import base64
from pdf2image import convert_from_path
import tempfile

# Create your views here.
def home(request):
    return render(request, 'base/header.html')

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated: # if tries to login beeing logged in
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")
        
        user = authenticate(request, username=username, password=password) # will return error, or if match, return a user object
        if user:
            login(request, user) # add a user in the session, and logs it in
            return redirect('home')
        else:
            messages.error(request, "Username or password does not exist")

        
    context = {'page': page}
    return render(request, 'base/login_register.html', context)

def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # we save the form to acess the user
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
            
    return render(request, 'base/login_register.html', {'form': form}) 


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
# def show_doc(request, doc_id):
#     # Assuming your model has a FileField for storing PDFs
#     document = Document.objects.get(doc_id=doc_id)
#     # Access the FileField directly
#     pdf_content = document.doc.open('rb').read()  # 'doc' is the FileField
#     # Encode PDF to base64
#     b64_pdf = base64.b64encode(pdf_content).decode('utf-8')
#     return render(request, 'base/pdf_viewer.html', {'pdf_content': b64_pdf})

def show_doc(request, doc_id):
    document = get_object_or_404(Document, doc_id=doc_id)
    # Open the PDF file
    pdf_content = document.doc.open('rb')
    
    # Convert PDF to images (each page becomes an image)
    images = convert_from_path(pdf_content.name, poppler_path=r'C:\Program Files (x86)\Release-24.02.0-0\poppler-24.02.0\Library\bin')
    
    image_data = []
    for image in images:
        # Save image to temporary file
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp:
            image.save(temp.name, 'PNG')
            temp.seek(0)
            # Read image data and encode in base64
            encoded_string = base64.b64encode(temp.read()).decode('utf-8')
            image_data.append(encoded_string)

    return render(request, 'base/pdf_viewer.html', {'image_data': image_data})