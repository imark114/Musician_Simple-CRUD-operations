from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.addAlbum, name = 'add_album'),
    path('edit/<int:id>', views.editAlbum, name='edit_album')
]
