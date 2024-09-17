from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('<str:room>/' , views.room , name='room'),
    path('checkRoom' , views.checkRoom, name='checkRoom'),
    path('send' , views.send , name='send'),
    path('getMessages/<str:room>/', views.getMessages , name='getMessages')
]
