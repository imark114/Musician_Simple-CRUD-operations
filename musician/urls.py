from django.urls import path
from . import views
urlpatterns = [
    path('add/', views.add_musician, name= 'add_musician'),
    path('edit/<int:id>',views.editMusician, name='edit_musician'),
    path('delete/<int:id>', views.deleteMusician, name='delete_musician')
]
