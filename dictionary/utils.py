from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent


def get_words():
    file = open(os.path.join(BASE_DIR, 'dict.txt'), "r", encoding="utf-8").read().splitlines()
    # file = open("/home/dekkobraze/DjangoProjects/MAIDictionary/dict.txt", "r", encoding="utf-8").read().splitlines()
    words1 = []
    words2 = []
    for line in file:
        word1, word2 = line.split("-")
        words1.append(word1)
        words2.append(word2)
    return words1, words2
