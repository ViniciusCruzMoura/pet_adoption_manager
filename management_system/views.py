from django.shortcuts import render
from .models import Animal

# Create your views here.

def index(request):
    context = {
        'title': 'Adoção de Animais',
        'description': 'Hello World!!!',
        'animal_album': Animal.objects.all() or None,
    }
    return render(request, 'index.html', context)