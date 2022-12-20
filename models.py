"""Model for a deck of cards"""
from random import choice, shuffle
import itertools
from typing import List


class Deck:
    cards = []
    card = []

    @classmethod
    def __deck__(cls):
        ranks = [str(n) for n in range(2, 11)] + 'Jack Queen King Ace'.split()
        suits = 'Spades Diamonds Clubs Hearts'.split()
        deck = [[rank, suit] for rank in ranks for suit in suits]
        shuffle(deck)
        Deck.cards = [card for card in deck]

    @classmethod
    def __card__(cls):
        card = cls.cards[0]
        cls.card = card
        cls.cards.remove(card)

    @classmethod
    def __facecardnumvalueadd__(cls):
        face = 'Jack Queen King'.split()
        if cls.card[0] in face:
            cls.card.insert(0, '10')
        elif cls.card[0] == 'Ace':
            cls.card.insert(0, '11')
        else:
            return False


class BlackjackPerson(Deck):

    def __init__(self):
        hand_count = 1
        empty_hand = {
            "cards": [],
            "hand_value": 0,
            "hit_count": 0
        }
        self.hand = [empty_hand]

    def __hit__(self):
        for hand in self.hand:
            hand["cards"].append(Deck.card)
            print(f"you drew: {Deck.card}")
            Deck.__card__()

    def __handvaluecount__(self):
        for hand in self.hand:
            cards = [card for card in hand["cards"]]
            value = sum(int(card[0]) for card in cards)
            hand["hand_value"] = value

    def __hitcount__(self):
        for hand in self.hand:
            cards = [card for card in hand["cards"]]
            hand["hit_count"] = len(cards)

        #     def __str__(self):
        #         print('Your Hand:')
        #         for card in self.hand:
        #             print(f'{card[-2]} of {card[-1]}')
        #         print(f'Hand Value: {self.hand_value}')

        # class Dealer(BlackjackPerson):

        #     def __init__(self):
        #         super().__init__()

        #     def __valuewatch__(self):
        #         if self.handvalue < 17:
        #             self.__hit__()
        #             self.__facecardnumvalueadd__()
        #             self.__acevaluerefactor__()
        #             self.__handvaluecount__()
        #         else:
        #             pass

        # class Player(BlackjackPerson):

        #     def __init__(self):
        #         super().__init__()
        #         self.multihand = []

        #     def __handsplit__(self):
        #         for hit_count in self.hitcount:
        #             if hit_count == 2:
        #                 for hand in self.hand:
        #                     card_1 = hand[0]
        #                     card_2 = hand[1]
        #                     try:
        #                         assert card_1[0] == card_2[0]
        #                         for card in hand:
        #                             self.multihand.append([card])
        #                         self.hand = self.multihand
        #                         self.hit_count = None
        #                     except AssertionError:
        #                         print('No doubles...')
