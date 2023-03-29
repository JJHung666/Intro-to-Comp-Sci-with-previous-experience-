# Test.py
from random import *
deck_of_cards = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K']
while len(deck_of_cards) > 0:
	print(deck_of_cards.pop(randrange(0,len(deck_of_cards))))