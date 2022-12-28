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

    @classmethod
    def __cardchoice__(cls, position):
        card = cls.cards[position]
        cls.card = card
        cls.cards.remove(card)


class BlackjackPerson(Deck):

    def __init__(self):
        self.hand = [{
            "cards": [],
            "hand_value": 0,
            "hit_count": 0
        }]

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

    def __acevaluerefactor__(self):
        for hand in self.hand:
            cards = [card for card in hand["cards"]]
            for card in cards:
                if hand["hand_value"] > 21 and card[0] == '11':
                    card[0] = '1'
                    value = sum(int(card[0]) for card in cards)
                    hand["hand_value"] = value
                else:
                    pass
            print(f'refactor complete. hand value is {hand["hand_value"]}')


class Dealer(BlackjackPerson):

    def __init__(self):
        super().__init__()

    def __valuewatch__(self):
        if self.hand[0]["hand_value"] < 17:
            self.__hit__()
            self.__facecardnumvalueadd__()
            self.__acevaluerefactor__()
            self.__handvaluecount__()
        else:
            pass


class Player(BlackjackPerson):

    def __init__(self):
        super().__init__()

    def __handsplit__(self):
        for hand in self.hand:
            if hand["hit_count"] == 2:
                card_1 = hand["cards"][0]
                card_2 = hand["cards"][1]
                try:
                    assert card_1[0] == card_2[0]
                    self.hand.append(
                        {"cards": [card_2], "hand_value": int(card_2[0]), "hit_count": 1})
                    hand["cards"].remove(card_2)
                except AssertionError:
                    print('No doubles...')


def test_run():
    Deck.__deck__()
    Deck.__card__()
    b = BlackjackPerson()
    Deck.__facecardnumvalueadd__()
    b.__hit__()
    Deck.__card__()
    Deck.__facecardnumvalueadd__()
    b.__hit__()
    Deck.__card__()
    Deck.__facecardnumvalueadd__()
    b.__hit__()
    b.__handvaluecount__()
    b.__hitcount__()
    b.__acevaluerefactor__()
    print(b.hand)


test_run()
