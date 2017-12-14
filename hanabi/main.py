import logging
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

logger = logging.getLogger(__name__)


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
        logger.info("Player {}'s turn".format(
            current_player_index+1))
        current_player = players[current_player_index]
        action = current_player.choose_action()

        if action == 'discard':
            card = current_player.discard_card()
            logger.info("Player chose to discard {}".format(card))

        elif action == 'play':
            card = current_player.play_card()
            stack = firework_stacks[card.color]
            logger.info("Player played {}".format(card))
            if card.rank == len(stack)+1:
                stack.append(card)
                logger.info("Success!")
            else:
                remaining_fuse_tokens -= 1
                logger.info("Oops. Remaining fuse tokens: {}".format(
                    remaining_fuse_tokens))

        if not current_player.has_enough_cards():
            current_player.receive_cards(deck.pop())

        for player in players:
            player.update_priors(
                dict(
                    (i, _player.cards)
                    for i, _player in enumerate(players)
                    if _player != player
                ),
                firework_stacks,
                remaining_clue_tokens,
                remaining_fuse_tokens,
            )

        current_player_index = (current_player_index+1) % num_players

    logger.info("Game over!")

    final_score = sum(len(stack) for stack in firework_stacks.values())
    logger.info("Final score: {}".format(final_score))


def set_up_logging():
    standard_handler = logging.StreamHandler()
    formatter = logging.Formatter(
        '%(asctime)s: %(message)s',
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    standard_handler.setFormatter(formatter)
    logger.addHandler(standard_handler)
    logger.setLevel(logging.INFO)


if __name__ == '__main__':
    set_up_logging()
    new_game()
