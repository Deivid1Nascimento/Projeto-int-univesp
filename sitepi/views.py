from django.shortcuts import render, redirect
from sitepi.forms import Faculdadesform
from sitepi.models import Faculdades
from django.core.paginator import Paginator
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'index.html')


def form(request):
    data = {}
    data['form'] = Faculdadesform()
    return render(request, 'form.html', data)


def create(request):
    form = Faculdadesform(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('resultados')


def resultados(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Faculdades.objects.filter(curso__icontains=search)
    else:
        all = Faculdades.objects.all()
        paginator = Paginator(all, 8)
        pages = request.GET.get('page')
        data['db'] = paginator.get_page(pages)
    return render(request, 'resultados.html', data)


def visualizar(request, pk):
    data = {}
    data['db'] = Faculdades.objects.get(pk=pk)
    return render(request, 'visualizar.html', data)


def editar(request, pk):
    data = {}
    data['db'] = Faculdades.objects.get(pk=pk)
    data['form'] = Faculdadesform(instance=data['db'])
    return render(request, 'form.html', data)


def atualizar(request, pk):
    data = {}
    data['db'] = Faculdades.objects.get(pk=pk)
    form = Faculdadesform(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()

        messages.info(request, 'Dados Atualizado!' )

    return redirect('resultados')


def apagar(request, pk):
    db = Faculdades.objects.get(pk=pk)
    db.delete()
    return redirect('resultados')
