"""Hanabi player interface."""

class Player(object):
    def __init__(self, card_limit):
        self.cards = []
        self.limit = card_limit

    def play_card(self):
        pass

    def discard_card(self):
        pass

    def give_clue(self):
        pass

    def receive_cards(self, *cards):
        pass
