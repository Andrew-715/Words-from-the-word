class Player:
    def __init__(self, user_name=''):
        self.user_name = user_name
        self.user_answer = []

    def __repr__(self):
        return f'''Player({self.user_name}, {self.user_answer})'''

    def count_words_used(self):
        return len(self.user_answer)

    def adding_word_in_user_answer(self, input):
        self.user_answer.append(input)

    def checking_use_word(self, input):
        return input in self.user_answer

    def get_name(self):
        return self.user_name
