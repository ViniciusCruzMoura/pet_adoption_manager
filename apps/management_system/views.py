from django.shortcuts import render
from .models import Animal

# Create your views here.

def index(request):
    context = {
        'title': 'Sistema de Gestão de Adoção de Animais',
        'description': '',
        # 'animal_album': Animal.objects.filter().order_by('-id')[:10] or None,
    }
    return render(request, 'index.html', context)