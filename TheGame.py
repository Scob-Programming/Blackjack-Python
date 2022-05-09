
# import itertools
import random


# Creates Card class to store suit and value of individual cards
class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print('{} of {}'.format(self.value, self.suit))


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def deal_card(self):
        return self.cards.pop()


class Player(object):
    def __init__(self, name, score):
        self.name = name
        self.hand = []
        self.secondhand = []
        self.score = score

    def show_name(self):
        print("Player: {}\nScore: {}".format(self.name, self.score))

    def draw(self, deck):
        self.hand.append(deck.deal_card())
        return self

    def show_hand(self):
        for card in self.hand:
            card.show()


class Dealer(object):
    def __init__(self, name, score):
        self.name = name
        self.hand = []
        self.secondhand = []
        self.score = score

    def show_name(self):
        print("Dealer: {}\nScore: {}".format(self.name, self.score))

    def draw(self, deck):
        self.hand.append(deck.deal_card())
        return self

    def show_hand(self):
        for card in self.hand:
            card.show()


class Blackjack(object):
    def __init__(self):
        self.pot = []
        self.round = []

    def hit(self):
        return self

    def stand(self):
        return self

    def double(self):
        return self

    def card_dict(self):
        return self

    def score(self):
        return self

    def score_compare(self):
        return self

    def bet(self):
        return self


dealer = Dealer("Michele", 0)
player = Player("Paul", 0)

deck_temp = Deck()
deck_temp.shuffle()
deck_temp.show()
print('Deck Length: ', len(deck_temp.cards))
print("\n")

player.draw(deck_temp).draw(deck_temp)
player.show_name()
player.show_hand()
print("\n")

dealer.draw(deck_temp).draw(deck_temp)
dealer.show_name()
dealer.show_hand()

print("\n")
deck_temp.show()

blackjack = Blackjack()

print('Deck Length: ', len(deck_temp.cards))

