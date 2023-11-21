from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('',views.show_posts_all,name='index'),
    path('add_post/',views.add_new_post,name='add_new_post'),
]