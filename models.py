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
        self.hand = []
        self.hit_count = 0
        self.hand_value = 0

    def __hit_count__(self):
        self.hit_count = len(self.hand) if self.hand != [] else 0

    def __hand_value__(self):
        self.hand_value = sum(int(value[0]) for value in self.hand)

    def __str__(self):
        print('Your Hand:')
        for card in self.hand:
            print(f'{card[-2]} of {card[-1]}')
        print(self.hand_value)

    def __hit__(self):
        randomcard = choice(Deck.cards)
        self.hand.append(randomcard)
        Deck.cards.remove(randomcard)
        print(f"you drew: {randomcard}")
        return

    def __facecardnumvalueadd__(self):
        for card in self.hand:
            for face in 'Jack Queen King'.split():
                while len(card) == 2:
                    if face in card:
                        card.insert(0, '10')
                    elif 'Ace' in card:
                        card.insert(0, '11')
                    break

    def __acevaluerefactor__(self):
        while self.hand_value > 21:
            for value in self.hand:
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
            self.__hand_value__()
        else:
            pass


class Player(BlackjackPerson):

    def __init__(self):
        super().__init__()
        self.multihand = []
        self.multihitcount = []
        self.multihandvalue = []

    def __handsplit__(self):
        if self.hit_count == 2:
            card_1 = self.hand[0]
            card_2 = self.hand[1]
            try:
                assert card_1[0] == card_2[0]
                for card in self.hand:
                    self.multihand.append([card])
                self.hand = self.multihand
                self.hit_count = None
            except AssertionError:
                print('No doubles...')
        else:
            pass

    def __multisplit__(self):
        for hit_count in self.multihitcount:
            if hit_count == 2:
                for each_hand in self.multihand:
                    each_card_1 = each_hand[0]
                    each_card_2 = each_hand[1]
                    try:
                        assert each_card_1[0] == each_card_2[0]
                        self.multihand.append([each_card_1])
                        each_hand.remove(each_card_1)
                        self.hand = self.multihand
                    except AssertionError:
                        print('No doubles...')
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
