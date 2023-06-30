from utils import load_random_word
from player import Player


data_json = 'https://www.jsonkeeper.com/b/UV97'

if __name__ == '__main__':
    user_name = input('Введите имя игрока: ')
    player = Player(user_name)
    print()
    print(f'Привет, {player.get_name()}')

    basic_word = (load_random_word(data_json))

    print(f'Составьте {basic_word.counting_subwords()} слов из слова {basic_word.get_word().upper()}')
    print(f'Слова должны быть не короче 3 букв')
    print(f'Чтобы закончить игру, угадайте все слова или напишите "stop" или "стоп"')
    print('Поехали, ваше первое слово?')


while player.number_words_used() < basic_word.counting_subwords(): # цикл для принятия слов от пользователя и последующей проверки их

    user_input = input().strip().lower()

    if user_input in ['stop', 'стоп']: # при получении стоп-слова завершаем приложение
        break

    elif len(user_input) < 3:
        print('Слово слишком короткое')
        continue

    elif not basic_word.has_subword(user_input):
        print('Нет такого слова')

    elif player.checking_use_word(user_input):
        print('Слово уже использовано')

    else:
        print('Верно')
        player.user_word(user_input)

print(f'Игра закончена! Вы угадали {player.number_words_used()} слов')
