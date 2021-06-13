from blackjack_package.card_class import Card
from random import randint

class Deck:
	
	suits = ['heart', 'diamonds', 'spades', 'clubs']
	values = ['ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'jack', 'queen', 'king']
	deck_list = []

	def __init__(self):
		for suit in Deck.suits:
			for value in Deck.values:
				Deck.deck_list.append(Card(value, suit))

	def get_card_value(self):
		#Getting a random card and removing it from deck
		#Returning the card's value/rank because the color doesn't matter
		try:
			return Deck.deck_list.pop(randint(0, len(Deck.deck_list)-1)).get_value()
		except:
			print(f'ERROR!\n{len(Deck.deck_list)}')

	def reset_deck(self):
		Deck.deck_list.clear()
		for suit in Deck.suits:
			for value in Deck.values:
				Deck.deck_list.append(Card(value, suit))

				




