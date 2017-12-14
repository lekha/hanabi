"""Hanabi player interface."""
import random

from hanabi.errors import TooManyCardsInHandError

class Player(object):
    def __init__(self, card_limit):
        self.cards = []
        self.limit = card_limit

    def has_enough_cards(self):
        return self.cards == self.limit

    def choose_action(self):
        raise NotImplementedError

    def play_card(self):
        raise NotImplementedError

    def discard_card(self):
        raise NotImplementedError

    def give_clue(self):
        raise NotImplementedError

    def receive_cards(self, *cards):
        if len(self.cards)+len(cards) <= self.limit:
            self.cards.extend(cards)
        else:
            raise TooManyCardsInHandError(
                "Maximum of %s cards allowed in hand" % self.limit)

    def update_priors(
            self, player_cards, firework_stacks, clue_tokens, fuse_tokens):
        return None


class DrunkPlayer(Player):
    def choose_action(self):
        actions = ['discard', 'play']
        action_to_perform = random.choice(actions)
        return action_to_perform

    def discard_card(self):
        assert len(self.cards) != 0
        discarded_card = self.cards.pop(0)
        return discarded_card

    def play_card(self):
        assert len(self.cards) != 0
        card_to_play = self.cards.pop(0)
        return card_to_play
