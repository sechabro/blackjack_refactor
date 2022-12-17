from models import Deck
import itertools


def test_deck_length():
    d = Deck()
    assert len(d.cards) == 52


def test_facecardnumvalueadd_functionality():
    d = Deck()
    iter_deck = iter(d.cards)
    next_card = None
    faces = 'Jack Queen King Ace'.split()
    while True:
        next_card = next(iter_deck)
        if next_card[0] in faces:
            d.card = next_card
            d.__facecardnumvalueadd__()
            assert len(d.card) == 3
            break
        else:
            continue
