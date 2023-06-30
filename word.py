class BasicWord:
    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords


    def __repr__(self):
        return f'''BasicWord({self.word}, {len(self.subwords)})'''


    def has_subword(self, attempt):
        """
        Проверка введённого слова в списке подпустимых подслов
        """
        return attempt.strip().lower() in self.subwords


    def counting_subwords(self):
        """
        Подсчёт количества подслов
        """
        return len(self.subwords)


    def get_word(self):
        """
        Возвращает полное слово
        """
        return self.word
