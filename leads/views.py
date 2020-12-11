from django.shortcuts import render, redirect
from .forms import ClienteForm


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


def bienvenida(request):
    return render(request, 'leads/bienvenida.html', {})
