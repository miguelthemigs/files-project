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
import json


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
    badge_scores = [150, 500, 1000]
    '''
    Tente obter a pontuação para o user especificado.
    Se essa pontuação não existir, crie uma nova pontuação para esse user com points inicializados em 0.
    Atribua o objeto encontrado ou criado a user_points.
    Atribua True a created se um novo objeto foi criado, ou False se o objeto já existia e foi apenas recuperado.
    '''
    context = {
        'user': user,
        'points': user_points.points,  # Adiciona os pontos ao contexto
        'badge_scores': badge_scores,
    }
    return render(request, 'base/profile.html', context)



def show_doc(request, doc_id=None, page_number=1, randomize=0, input_type=None, input_id=None):
    if request.method == 'POST':
        tags_json = request.POST.get('tags')
        if tags_json:
            tag_list = json.loads(tags_json)
            for tag in tag_list:
                form_data = {'input_content': tag, 'input_type': input_type}
                form = InputLogForm(form_data)
                if form.is_valid():
                    input_log = form.save(commit=False)
                    input_log.user_id = request.user.id
                    input_log.doc_id = get_object_or_404(Document, pk=doc_id)
                    input_log.input_type = input_type
                    input_log.save()
            return redirect('show-doc-randomize')
        else:
            form = InputLogForm(request.POST)
            if form.is_valid():
                input_log = form.save(commit=False)
                input_log.user_id = request.user.id
                input_log.doc_id = get_object_or_404(Document, pk=doc_id)
                input_log.input_type = input_type
                input_log.save()

                if request.user.is_authenticated:
                    user_points, created = UserPoints.objects.get_or_create(user=request.user)
                    user_points.points += 100
                    user_points.save()

                return redirect('show-doc-randomize')

    if randomize:
        # Retrieve a random document that is not audiovisual (0) or sonoro (3)
        documents_length = Document.objects.count()
        while True:
            random_index = random.randint(0, documents_length - 1)
            document = Document.objects.all()[random_index]
            if document.doc_type not in [0, 3]:
                doc_id = document.doc_id
                break
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
    images = convert_from_path(pdf_path, first_page=page_number, last_page=page_number, dpi=dpi, poppler_path = r'C:\Program Files (x86)\Release-24.02.0-0\poppler-24.02.0\Library\bin')#poppler_path=r'C:\Program Files (x86)\Release-24.02.0-0\poppler-24.02.0\Library\bin')

    image_data = []
    for image in images:
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp:
            image.save(temp.name, 'PNG')
            temp.seek(0)
            encoded_string = base64.b64encode(temp.read()).decode('utf-8')
            image_data.append(encoded_string)
    form = InputLogForm()
    if input_type is not None:
        if input_type != 4:
            return render(request, 'base/input.html', {
            'image_data': image_data,
            'total_pages': len(pdf.pages),
            'doc_id': doc_id,
            'current_page': page_number,
            'input_type': input_type,
            'form': form,
            }, )
        else:
            aleatorio = random.randint(0,1)
            input_object = InputLog.objects.filter(input_type=4, doc_id=doc_id)
            if len(input_object) == 0:
                aleatorio = 1
            input_object = input_object[0]

            if aleatorio:
                return render(request, 'base/input.html', {
                'image_data': image_data,
                'total_pages': len(pdf.pages),
                'doc_id': doc_id,
                'current_page': page_number,
                'input_type': input_type,
                'form': form,
                }, )
            else:
                return render(request, 'base/avaliar.html', {
                'image_data': image_data,
                'total_pages': len(pdf.pages),
                'doc_id': doc_id,
                'current_page': page_number,
                'input_type': input_type,
                'input_id': input_object.input_id,
                'input_content':input_object.input_content,
                }, )
    
    else:
        return render(request, 'base/home.html', {
            'image_data': image_data,
            'total_pages': len(pdf.pages),
            'doc_id': doc_id,
            'current_page': page_number
        })
        
