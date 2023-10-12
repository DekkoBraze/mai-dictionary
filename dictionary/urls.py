from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="main"),
    path('home/', index, name="main"),
    path('words_list/', words_list, name='words_list'),
    path('add_word/', new_word, name='add_word')
]