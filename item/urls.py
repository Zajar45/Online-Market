from django.urls import path
from . import views


app_name = 'item'

urlpatterns = [

    path('', views.items, name='items'),
    path('<int:pk>/', views.details, name='detail'),
    path('newitem/', views.new, name='new-item'),
    path('Edit/<int:pk>/', views.edit, name='edit-item'),
    path('Delete/<int:pk>/', views.delete, name='delete-item'),
]