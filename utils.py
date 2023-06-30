import random
import requests
from word import BasicWord


def load_json_from_jk(path): # загружает данные по ссылке и возвращает их в виде списка или словаря
    response = requests.get(path)
    response_json = response.json()
    return response_json


def load_random_word(path): # генерирует случайные слова и подслова
    all_words = load_json_from_jk(path)
    random_word = random.choice(all_words)
    word = random_word['word']
    subwords = random_word['subwords']
    basic_word = BasicWord(word, subwords)
    return basic_word
