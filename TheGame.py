
#import itertools
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

    def dealCard(self):
        return self.cards.pop()

class Player(object):
    def __init__(self, name, score):
        self.name = name
        self.hand = []
        self.secondhand = []
        self.score = score

    def showName(self):
        print("Player: {}\nScore: {}".format(self.name, self.score))

    def draw(self, deck):
        self.hand.append(deck.dealCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

class Dealer(object):
    def __init__(self, name, score):
        self.name = name
        self.hand = []
        self.secondhand = []
        self.score = score

    def showName(self):
        print("Dealer: {}\nScore: {}".format(self.name, self.score))

    def draw(self, deck):
        self.hand.append(deck.dealCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

class Blackjack(object):
    def __init__(self):
        self.pot = []
        self.round = []

    def hit(self):
        return self.draw()

    def stand(self):
        return self

    def double(self):
        return self

    def cardDict(self):
        return self

    def score(self):
        return self

    def scoreCompare(self):
        return self

    def bet(self):
        return self






deck = Deck()
deck.shuffle()
# deck.show()

dealer = Dealer("Michele", 0)
player = Player("Paul", 0)
player.draw(deck).draw(deck)
player.showHand()
player.showName()
dealer.draw(deck).draw(deck)
dealer.showHand()
dealer.showName()

blackjack = Blackjack()

blackjack(player)
player.showHand()

