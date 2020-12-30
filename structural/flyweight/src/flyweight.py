from abc import ABC, abstractmethod


class AbstractFlyweight(ABC):
    def __init__(self, letter):
        self.letter = letter

    @abstractmethod
    def render_letter(self):
        pass


class LetterFlyweight(AbstractFlyweight):
    def render_letter(self):
        print(self.letter, end='')


class FlyweightFactory:
    def __init__(self):
        self.__cache = {}

    def get_letter(self, letter):
        if letter not in self.__cache:
            self.__cache[letter] = LetterFlyweight(letter)

        return self.__cache[letter]

    def get_cache_size(self):
        return len(self.__cache)
