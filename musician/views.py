from django.shortcuts import render,redirect
from . import forms
from .models import Musician
# Create your views here.
def add_musician(request):
    if request.method == 'POST':
        musicianForm = forms.AddMusician(request.POST)
        if musicianForm.is_valid():
            musicianForm.save()
            return redirect('add_musician')
    musicianForm = forms.AddMusician()
    return render(request,'add_musician.html',{'form': musicianForm})

def editMusician(request, id):
    musician = Musician.objects.get(pk=id)
    musician_form = forms.AddMusician(instance= musician)
    if request.method == 'POST':
        musician_form = forms.AddMusician(request.POST,instance= musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('home')
    return render(request,'add_musician.html', {'form': musician_form})

def deleteMusician(request, id):
    musician =Musician.objects.get(pk=id)
    musician.delete()
    return redirect('home')
