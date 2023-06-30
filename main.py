from utils import load_random_word
from player import Player

"""Создаём переменную для добавления слов с подсловами с внешнего источника"""
data_json = 'https://www.jsonkeeper.com/b/UV97'


if __name__ == '__main__':
    """
    Предлагаем игроку ввести его имя и приветствуем его
    """
    user_name = input('Введите имя игрока: ')
    player = Player(user_name)
    print()
    print(f'Привет, {player.get_name()}')
    """
    Вызываем функцию для рандомизации полученных слов и добавляем её в переменную
    """
    basic_word = (load_random_word(data_json))
    """
    Пишем необходимый код программы с указанием нужного количества подслов и ключевого слова
    """
    print(f'Составьте {basic_word.counting_subwords()} слов из слова {basic_word.get_word().upper()}')
    print(f'Слова должны быть не короче 3 букв')
    print(f'Чтобы закончить игру, угадайте все слова или напишите "stop" или "стоп"')
    print('Поехали, ваше первое слово?')

"""Создаём цикл для принятия слов от пользователя и последующей проверки их"""
while player.number_words_used() < basic_word.counting_subwords():

    user_input = input().strip().lower()

    if user_input in ['stop', 'стоп']:
        """Получаем от пользователя стоп-слово для выхода из программы, если это необходимо"""
        break

    elif len(user_input) < 3:
        """Выводим сообщение, если слово короче 3-х букв"""
        print('Слово слишком короткое')
        continue

    elif not basic_word.has_subword(user_input):
        """Выводим сообщение, если слово нет в списке подслов"""
        print('Нет такого слова')

    elif player.checking_use_word(user_input):
        """Выводим сообщение, если слово уже было использовано"""
        print('Слово уже использовано')

    else:
        """Если слово верно, то выводим соответствующее сообщение и добавляем его в статистику"""
        print('Верно')
        player.user_word(user_input)

print(f'Игра закончена! Вы угадали {player.number_words_used()} слов')
