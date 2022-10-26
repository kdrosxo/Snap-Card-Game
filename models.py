from enum import Enum
import pygame
import random

class Shapes(Enum):
    CLUB = 0
    SPADE = 1
    HEART = 2
    DIAMOND =3

class Card:
    shape = None
    value = None
    image = None

    def __init__(self,shape,value):
        self.shape = shape
        self.value = value
        self.image = pygame.image.load('images/' + self.shape.name + '-' + str(self.value) + '.svg')


class Deck:
    cards = None

    def __init__(self):
        self.cards = []
        for shape in Shapes:
            for value in range(1,14):
                self.cards.append(Card(shape,value))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop()

    def length(self):
        return len(self.cards)

    
class Pile:
    cards = None

    def __init__(self):
        self.cards = []

    def add(self,card):
        self.cards.append(card)

    def peek(self):
        if (len(self.cards)>0):
            return self.cards[-1]
        else:
            return None

    def popAll(self):
         return self.cards

    def clear(self):
        self.cards = []

    def isSnap(self):
        if (len(self.cards)>1):
            return (self.cards[-1].value == self.cards[-2].value)
        return False


class Player:
    hand = None
    flipKey = None
    snapKey = None
    name = None

    def __init__(self,name,flipKey,snapKey):
        self.hand = []
        self.name = name
        self.flipKey = flipKey
        self.snapKey = snapKey

    def draw(self,deck):
        self.hand.append(deck.deal())

    def play(self):
        return self.hand.pop(0)

    



