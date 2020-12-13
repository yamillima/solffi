from django.shortcuts import render, redirect
from .forms import ClienteForm, InversionistaForm


def index(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bienvenida')
        else:
            form = ClienteForm()
            return render(request, 'leads/index.html', {'ClienteForm': form})
    else:
        form = ClienteForm()
        return render(request, 'leads/index.html', {'ClienteForm': form})


def inversionistas(request):
    if request.method == "POST":
        form = InversionistaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bienvenida')
        else:
            form = InversionistaForm()
            return render(request, 'leads/inversionistas.html', {'InversionistaForm': form})
    else:
        form = InversionistaForm()
        return render(request, 'leads/inversionistas.html', {'InversionistaForm': form})


def bienvenida(request):
    return render(request, 'leads/bienvenida.html', {})
