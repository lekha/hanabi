from collections import namedtuple


Card = namedtuple('Card', ['color', 'rank'])

COLORS = {'blue', 'green', 'red', 'white', 'yellow'}


def new_deck():
    deck = []
    for color in COLORS:
        for rank in [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]:
            deck.append(Card(color, rank))
    return deck


if __name__ == '__main__':
    deck = new_deck()
