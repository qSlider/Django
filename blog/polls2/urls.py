from django.urls import path
from . import views
from .views import add_post , post_detail , homepage , author_page , add_like

urlpatterns = [
    path('', views.index, name='polls2-index'),
    path('add_post' , add_post ,name='add_post'),
    path('post/<int:pk>' , post_detail , name='post_detail'),
    path('homepage/', homepage, name='homepage'),
    path('author/<int:pk>/',author_page, name='author_page'),
    path('add_like/<int:pk>/', add_like , name ='add_like'),
]