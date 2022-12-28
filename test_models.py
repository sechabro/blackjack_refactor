from models import Deck, BlackjackPerson, Player
import itertools


def test_deck_length():
    Deck.__deck__()
    assert len(Deck.cards) == 52


def test_facecardnumvalueadd_functionality():
    Deck.__deck__()
    iter_deck = iter(Deck.cards)
    next_card = None
    faces = 'Jack Queen King Ace'.split()
    while True:
        next_card = next(iter_deck)
        if next_card[0] in faces:
            Deck.card = next_card
            Deck.__facecardnumvalueadd__()
            assert len(Deck.card) == 3
            break
        else:
            print(len(Deck.card))
            continue


def test_BlackjackPerson_hit_functionality():
    Deck.__deck__()
    Deck.__card__()
    b = BlackjackPerson()
    b.__hit__()
    assert b.hand[0]["cards"][0] != Deck.card


def test_BlackjackPerson_hitcount():
    Deck.__deck__()
    Deck.__card__()
    b = BlackjackPerson()
    b.__hit__()
    Deck.__facecardnumvalueadd__()
    b.__hit__()
    b.__hitcount__()
    assert len(b.hand[0]["cards"]) == b.hand[0]["hit_count"]


def test_BlackjackPerson_handvalue():
    Deck.__deck__()
    Deck.__card__()
    Deck.__facecardnumvalueadd__()
    b = BlackjackPerson()
    b.__hit__()
    Deck.__facecardnumvalueadd__()
    b.__hit__()
    b.__handvaluecount__()
    assert sum(int(card[0]) for card in b.hand[0]
               ["cards"]) == b.hand[0]["hand_value"]


def test_BlackjackPerson_acevaluerefactor():
    b = BlackjackPerson()
    b.hand = [{'cards': [['11', 'Ace', 'Hearts'], [
        '11', 'Ace', 'Clubs']], 'hand_value': 22, 'hit_count': 2}]
    b.__acevaluerefactor__()
    assert b.hand[0]["hand_value"] == 12


def test_BlackjackPerson_acevaluerefactor_no_aces():
    b = BlackjackPerson()
    b.hand = [{'cards': [['10', 'Jack', 'Hearts'], [
        '10', 'Queen', 'Clubs'], ['6', 'Hearts']], 'hand_value': 26, 'hit_count': 3}]
    b.__acevaluerefactor__()
    assert b.hand[0]["hand_value"] == 26


def test_Player_handsplit_single_hand():
    b = BlackjackPerson()
    p = Player()
    p.hand = [{
        "cards": [['9', 'Spades'], ['9', 'Clubs']],
        "hand_value": 18,
        "hit_count": 2
    }]
    p.__handsplit__()
    assert p.hand[1]["cards"][0] == ['9', 'Clubs']


def test_Player_handsplit_multi_hand():
    b = BlackjackPerson()
    p = Player()
    p.hand = [{
        "cards": [['9', 'Spades'], ['8', 'Clubs']],
        "hand_value": 17,
        "hit_count": 2
    },
        {
        "cards": [['7', 'Spades'], ['2', 'Clubs']],
        "hand_value": 9,
        "hit_count": 2
    },
        {
        "cards": [['6', 'Spades'], ['6', 'Clubs']],
        "hand_value": 18,
        "hit_count": 2
    }]
    p.__handsplit__()
    p.__handvaluecount__()
    assert p.hand[2]["hand_value"] == 6
    assert p.hand[3]["hand_value"] == 6
