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
        shuffle(cls.cards)
        return cls.cards


class BlackjackPerson(Deck):

    def __init__(self):
        self._hand = []
        self._hit_count = 0
        self._hand_value = 0

    def __hit_count__(self):
        if self._hand != []:
            for _ in range(1, len(self._hand)+1):
                self._hit_count += 1

    def __hand_value__(self):
        self._hand_value = sum(int(value[0]) for value in self._hand)

    def __hit__(self):
        randomcard = choice(Deck.cards)
        self._hand.append(randomcard)
        Deck.cards.remove(randomcard)
        print(f"you drew: {randomcard}")
        return

    def __facecardnumvalueadd__(self):
        for card in self._hand:
            for face in 'Jack Queen King'.split():
                while len(card) == 2:
                    if face in card:
                        card.insert(0, '10')
                    elif 'Ace' in card:
                        card.insert(0, '11')
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

    def __getitem__(self, position):
        pick = Deck.cards[position]
        self.hand.append(pick)
        Deck.cards.remove(pick)


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
        self.multihand = []

    def __handsplit__(self):
        if self.hit_count == 2:
            card_1 = self.hand[0]
            card_2 = self.hand[1]
            try:
                assert card_1[0] == card_2[0]
                for card in self.hand:
                    self.multihand.append([card])
                self.hand = self.multihand
                self.hit_count = 1
            except AssertionError:
                print('No matching values.')
        else:
            pass

    def __multihit__(self):
        for hand in self.hand:
            randomcard = choice(Deck.cards)
            hand.append(randomcard)
            Deck.cards.remove(randomcard)
            print(f"you drew: {randomcard}")

    def __multifacecardnumvalueadd__(self):
        face = 'Jack Queen King'.split()
        for hand in self.hand:
            for card in hand:
                while len(card) == 2:
                    if face in card:
                        card.insert(0, '10')
                    elif 'Ace' in card:
                        card.insert(0, '11')
                    break


# *args
# def initialize():
#     d = Deck()
#     b = BlackjackPerson()
#     p = Player()
#     p.__getitem__(44)
#     p.__getitem__(44)
#     p.__facecardnumvalueadd__()
#     p.__hitcounter__()
#     p.__handsplit__()
#     print(p.hand)
#     p.__multihit__()
#     print(p.hand)
#     p.__facecardnumvalueadd__()
#     print(p.hand)

# d = Deck()
# b = BlackjackPerson()
# de = Dealer()


# def DealerPlay():
    # de.__calculatehand__()
    # de.__valuewatch__()
    # print(de.hand)


# DealerPlay()
# d = Deck()
# b = BlackjackPerson()
# de = Dealer()
# p = Player()
# initialize()
