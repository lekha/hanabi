from collections import namedtuple
from random import shuffle

from hanabi.players import DrunkPlayer


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
    discard_stack = []
    firework_stacks = {color: [] for color in COLORS}
    deck = new_deck()

    num_players = 3
    cards_per_hand = NUM_PLAYERS_TO_NUM_CARDS_PER_HAND[num_players]
    players = []
    for _ in range(num_players):
        players.append(DrunkPlayer(cards_per_hand))
        for _ in range(cards_per_hand):
            players[-1].receive_cards(deck.pop())

    def game_over():
        return not deck or remaining_fuse_tokens == 0

    shuffle(players)
    current_player_index = 0
    while not game_over():
        current_player = players[current_player_index]
        action = current_player.choose_action()
        if action == 'discard':
            card = current_player.discard_card()

        if not current_player.has_enough_cards():
            current_player.receive_cards(deck.pop())

        current_player_index = (current_player_index+1) % num_players


if __name__ == '__main__':
    new_game()
