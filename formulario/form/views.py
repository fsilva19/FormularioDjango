from django.shortcuts import render, redirect
from .forms import formularioView


def formBase(request):
    if request.method == 'POST':
        form = formularioView(request.POST)
        form.nome = request.POST.get('nome', None)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:    
        form = formularioView()
        return render(request, 'formbase.html', {'form': form})
    
    