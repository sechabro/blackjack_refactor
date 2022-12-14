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
        # shuffle(cls.cards)
        return cls.cards


class BlackjackPerson(Deck):

    def __init__(self):
        self.hand = [[]]
        self.hitcount = []
        self.handvalue = []

    def __hitcount__(self):
        self.hitcount.clear()
        for hand in self.hand:
            hand_hit_count = len(hand)
            self.hitcount.append(hand_hit_count)

    def __handvaluecount__(self):
        self.handvalue.clear()
        for hand in self.hand:
            value = 0
            for card in hand:
                card_value = int(card[0])
                value += card_value
            self.handvalue.append(value)

    def __hit__(self):
        for hand in self.hand:
            randomcard = choice(Deck.cards)
            hand.append(randomcard)
            Deck.cards.remove(randomcard)
            print(f"you drew: {randomcard}")

    def __facecardnumvalueadd__(self):
        face = 'Jack Queen King'.split()
        for hand in self.hand:
            for card in hand:
                while len(card) == 2:
                    if card[0] in face:
                        card.insert(0, '10')
                    elif card[0] == 'Ace':
                        card.insert(0, '11')
                    break

    def __acevaluerefactor__(self):
        for hand in self.hand:
            for value in self.handvalue:
                while value > 21:
                    for card in hand:
                        if card[0] == '11':
                            card[0] = '1'
                            value = sum(int(card[0]) for card in hand)
                        else:
                            continue
                    break

    def __str__(self):
        print('Your Hand:')
        for card in self.hand:
            print(f'{card[-2]} of {card[-1]}')
        print(f'Hand Value: {self.hand_value}')

    def __getitem__(self, position):
        for hand in self.hand:
            pick = Deck.cards[position]
            hand.append(pick)
            Deck.cards.remove(pick)


class Dealer(BlackjackPerson):

    def __init__(self):
        super().__init__()

    def __valuewatch__(self):
        if self.handvalue < 17:
            self.__hit__()
            self.__facecardnumvalueadd__()
            self.__acevaluerefactor__()
            self.__handvaluecount__()
        else:
            pass


class Player(BlackjackPerson):

    def __init__(self):
        super().__init__()
        self.multihand = []

    def __handsplit__(self):
        for hit_count in self.hitcount:
            if hit_count == 2:
                for hand in self.hand:
                    card_1 = hand[0]
                    card_2 = hand[1]
                    try:
                        assert card_1[0] == card_2[0]
                        for card in hand:
                            self.multihand.append([card])
                        self.hand = self.multihand
                        self.hit_count = None
                    except AssertionError:
                        print('No doubles...')
