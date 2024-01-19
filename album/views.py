from django.shortcuts import render, redirect
from . import forms
from . import models
# Create your views here.
def addAlbum(request):
    if request.method == 'POST':
        album_form = forms.AddAlbum(request.POST)
        if album_form.is_valid():
            album_form.save()
            return redirect('add_album')
    album_form = forms.AddAlbum()
    return render(request, 'add_album.html',{'form':album_form})

def editAlbum(request, id):
    ablum = models.Album.objects.get(pk=id)
    ablum_form = forms.AddAlbum(instance=ablum)
    if request.method == 'POST':
        album_form = forms.AddAlbum(request.POST, instance=ablum)
        if album_form.is_valid():
            album_form.save()
            return redirect('home')
    return render(request,'add_album.html',{'form': ablum_form})

