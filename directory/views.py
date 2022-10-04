from django.shortcuts import render
from directory.forms import DirectoryForm
from directory.models import Directory
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
# Create your views here.


def index(request):
    telephone = Directory.objects.all()
    context = {
        'contact': telephone
    }
    return render(request, 'directory/index.html', context)

def insert(request):
    form = DirectoryForm(request.POST or None, request.FILES or None)
    context = {
        'form': form
    }
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
    return render(request, 'directory/insert.html', context)

def remove(request, id):
    try:
        records = Directory.objects.get(id=id)
        records.delete()
        messages.success(request, 'Contact deleted')
        return redirect(reverse('index'))
    except:
        messages.success(request, 'Record not found')
        return redirect(reverse('index'))


def amend(request, id):
    instance = Directory.objects.get(id=id)
    form = DirectoryForm(request.POST or None,
                         request.FILES or None, instance=instance)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
    return render(request, 'directory/insert.html', context)



