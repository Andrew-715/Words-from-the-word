class Player:
    def __init__(self, user_name=''):
        self.user_name = user_name
        self.user_answer = []


    def __repr__(self):
        return f'''Player({self.user_name}, {self.user_answer})'''


    def number_words_used(self):
        """
        Получение количества использованных слов
        """
        return len(self.user_answer)


    def user_word(self, input):
        """
        Добавление слова в использованные слова
        """
        self.user_answer.append(input)


    def checking_use_word(self, input):
        """
        Проверка использования данного слова до этого
        """
        return input in self.user_answer


    def get_name(self):
        """
        Возвращает имя игрока
        """
        return self.user_name
