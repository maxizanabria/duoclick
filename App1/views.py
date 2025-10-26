from django.shortcuts import render, redirect
from .forms import ContactoForm
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Gracias! Pronto nos comunicaremos contigo.')
            return redirect('index')
    else:
        form = ContactoForm()
    return render(request, 'index.html', {'form': form})


def landing(request):
    return render(request, 'landing.html')


def ingresar(request):
    if request.method == "POST":
        return redirect('index')  # redirige a tu página principal
    return render(request, 'ingresar.html')
def home(request):
    return render(request, 'index.html')

def ingresar(request):
    return render(request, 'ingresar.html')