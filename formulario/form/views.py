from django.shortcuts import render
from django.http import HttpResponse
from .forms import formularioView


def formBase(request):
    if request.method == 'POST':    
        form = formularioView(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("enviou")
    else:
        form = formularioView()
        return render(request, 'formbase.html', {'form': form})


def pagTestando(request):
    return render(request, 'form/testando.html')
