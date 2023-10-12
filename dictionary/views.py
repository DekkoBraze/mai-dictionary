from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from pathlib import Path
import os
from .forms import *
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent

def index(request):
    return render(request, 'dictionary/index.html', context={'words_url': 'words_list'})


def words_list(request):
    file = open(os.path.join(BASE_DIR, 'dict.txt'), "r", encoding="utf-8").read().splitlines()
    #file = open("/home/dekkobraze/DjangoProjects/MAIDictionary/dict.txt", "r", encoding="utf-8").read().splitlines()
    words1 = []
    words2 = []
    for line in file:
        word1, word2 = line.split("-")
        words1.append(word1)
        words2.append(word2)
    words = list(zip(words1, words2))
    return render(request, 'dictionary/words_list.html', context={'words': words})


#def new_word(request):
#    if request.method == 'POST':
#        form = TranslationForm(request.POST)
#        if form.is_valid():
#            word1 = form.cleaned_data['word1']
#            word2 = form.cleaned_data['word2']
#            with open(os.path.join(BASE_DIR, 'dict.txt'), "a", encoding="utf-8") as file:
#                file.write(word1 + "-" + word2 + "\n")
#            return redirect('words_list')
#    else:
#        form = TranslationForm()

def new_word(request):
    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            word1 = form.cleaned_data['word1']
            word2 = form.cleaned_data['word2']
            with open(os.path.join(BASE_DIR, 'dict.txt'), "a", encoding="utf-8") as file:
                file.write(word1 + "-" + word2 + "\n")
            return redirect('words_list')
    else:
        form = TranslationForm()

    return render(request, 'dictionary/new_word.html', context={'form': form})