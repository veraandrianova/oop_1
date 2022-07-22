class Alphabet:

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        return self.letters

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self, lang, letters):
        super().__init__(lang, letters)

    def is_en_letter(self, letter):
        self.letter = letter
        if self.letter in self.letters:
            return True
        return False

    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        return f'Hello world'


d = Alphabet('eng', ['a', 'b', 'c'])
print(d.letters_num())
f = EngAlphabet('ru', ['а', 'б'])
print(f.print())
print(f.letters_num())
print(f.is_en_letter('п'))
print(f.example())
