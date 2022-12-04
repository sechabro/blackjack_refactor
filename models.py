"""Model for a deck of cards"""
from random import choice, shuffle
import itertools


class Deck:

    def __init__(self):
        self.cards = Deck.__createdeck__()

    @classmethod
    def __createdeck__(cls):
        ranks = [str(n) for n in range(2, 11)] + 'Jack Queen King Ace'.split()
        suits = 'Spades Diamonds Clubs Hearts'.split()
        cls.cards = [[rank, suit] for rank in ranks for suit in suits]
        return cls.cards


class BlackjackPerson(Deck):

    def __init__(self):
        self.hand = []
        self.hand_value = 0

    def __getitem__(self, position):
        pick = Deck.cards[position]
        self.hand.append(pick)

    def __hit__(self):
        self._randomcard = choice(Deck.cards)
        self.hand.append(self._randomcard)
        Deck.cards.remove(self._randomcard)
        return f"you drew: {self._randomcard}"

    def __showhand__(self):
        return self._hand, self._hand_value

    def __calculatehand__(self):
        self._hand_value = sum(int(value[0]) for value in self._hand)
        self.hand_value = self._hand_value
        return self.hand_value

    def __facecardnumvalueadd__(self):
        for value in self._hand:
            for face in 'Jack Queen King'.split():
                while len(value) == 2:
                    if face in value:
                        value.insert(0, '10')
                    elif 'Ace' in value:
                        value.insert(0, '11')
                    break

    def __acevaluerefactor__(self):
        while self.hand_value > 21:
            for value in self._hand:
                if value[0] == '11':
                    value[0] = '1'
                    self.__calculatehand__()
                else:
                    continue
            break


class Dealer(BlackjackPerson):

    def __init__(self):
        super().__init__()

    def __valuewatch__(self):
        if self.hand_value < 17:
            self.__hit__()
            self.__facecardnumvalueadd__()
            self.__acevaluerefactor__()
            self.__calculatehand__()
        else:
            pass


class Player(BlackjackPerson):

    def __init__(self):
        super().__init__()
        self.hit_count = 0
        self.multi_hand = []

    def __hitcounter__(self):
        self.hit_count = len(self.hand)

    def __handsplit__(self):
        if self.hit_count == 2:
            card_1 = self.hand[0][0]
            card_2 = self.hand[1][0]
            try:
                assert card_1 == card_2
            except AssertionError:
                print('No matching values.')
        else:
            pass
