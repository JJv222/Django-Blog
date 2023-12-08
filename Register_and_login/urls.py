from django.urls import path
from . import views

app_name = 'register_and_login'
urlpatterns = [
    path('',views.index,name='index'),
]
