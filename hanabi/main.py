from collections import namedtuple
from random import shuffle

from hanabi.players import Player


Card = namedtuple('Card', ['color', 'rank'])

COLORS = {'blue', 'green', 'red', 'white', 'yellow'}
NUM_PLAYERS_TO_NUM_CARDS_PER_HAND = {
    2: 5,
    3: 5,
    4: 4,
    5: 4,
}
STARTING_CLUE_TOKENS = 8
STARTING_FUSE_TOKENS = 3


def new_deck():
    deck = []
    for color in COLORS:
        for rank in [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]:
            deck.append(Card(color, rank))
    shuffle(deck)
    return deck


def new_game():
    remaining_clue_tokens = STARTING_CLUE_TOKENS
    remaining_fuse_tokens = STARTING_FUSE_TOKENS
    deck = new_deck()

    num_players = 3
    cards_per_hand = NUM_PLAYERS_TO_NUM_CARDS_PER_HAND[num_players]
    players = []
    for _ in range(num_players):
        players.append(Player(cards_per_hand))
        for _ in range(cards_per_hand):
            players[-1].receive_cards(deck.pop())


if __name__ == '__main__':
    new_game()
