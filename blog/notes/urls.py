from django.urls import path
from . import views
from .views import add_post2 , post_detail2 , homepage2 , author_page2 , add_like2 , add_note, note_list , homepagetest

urlpatterns = [
    path('', views.index, name='index'),
    path('add_post2', add_post2, name='add_post2'),
    path('post2/<int:pk>', post_detail2, name='post_detail2'),
    path('homepage2/', homepage2, name='homepage2'),
    path('author2/<int:pk>/', author_page2, name='author_page2'),
    path('add_like2/<int:pk>/', add_like2, name='add_like2'),
    path('add_note/', add_note, name='add_note'),
    path('note_list/', note_list, name='note_list'),
    path('notes/<int:pk>/', views.note_detail, name='note_detail'),
    path('notes/<int:pk>/delete/', views.delete_note, name='delete_note'),
    path('notes/<int:pk>/edit/', views.edit_note, name='edit_note'),
    path('homepagetest/', homepagetest, name='homepagetest'),
]