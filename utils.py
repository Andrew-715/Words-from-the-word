import random
import requests
from word import BasicWord


def load_json_from_jk(path):
    """
    Загружает данные по ссылке и возвращает их в виде списка или словаря
    :param path: путь к источнику данных
    :return:
    """
    response = requests.get(path)
    response_json = response.json()
    return response_json


def load_random_word(path):
    """
    Генерирует случайные слова и подслова, а также вызывает класс BasicWord
    """
    all_words = load_json_from_jk(path)
    random_word = random.choice(all_words)
    word = random_word['word']
    subwords = random_word['subwords']
    basic_word = BasicWord(word, subwords)
    return basic_word
