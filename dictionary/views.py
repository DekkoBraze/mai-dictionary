from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from pathlib import Path
import os
from .forms import *
from .utils import get_words, BASE_DIR
from django.urls import reverse_lazy
from django.http import HttpResponse


def index(request):
    return render(request, 'dictionary/index.html', context={'words_url': 'words_list'})


def words_list(request):
    words1, words2 = get_words()
    words = list(zip(words1, words2))
    return render(request, 'dictionary/words_list.html', context={'words': words})


def new_word(request):
    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            word1 = form.cleaned_data['word1']
            word2 = form.cleaned_data['word2']
            words1, words2 = get_words()
            if word1 in words1 and word2 in words2:
                return HttpResponse('Такой перевод уже есть в вашем словаре. Вы точно ничего не напутали?', status=401)
            with open(os.path.join(BASE_DIR, 'dict.txt'), "a", encoding="utf-8") as file:
                file.write(word1 + "-" + word2 + "\n")
            return redirect('words_list')
    else:
        form = TranslationForm()

    return render(request, 'dictionary/new_word.html', context={'form': form})
