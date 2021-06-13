from blackjack_package.deck_class import Deck
from time import sleep

class Player:

	#Every player will have a hand of Cards and every table will have a deck
	#The hand variable refers to the values of a players hand of cards
	
	deck = Deck()

	def __init__(self, hand = [], name='default'):
		self.name = name
		self.hand = hand

	def update_hand(self, num=1):
		#If num equals 1 then this method gets a card for player 1's hand else it get a card for the computers hand
		if(num == 1):
			print('Getting a card from the deck...')
			piece = Player.deck.get_card_value()
			sleep(1)
			print(f'The card you got is a {piece}')
			self.hand.append(piece)
		else:
			print('Getting a card from the deck...')
			self.hand.append(Player.deck.get_card_value())

	def greeting(self):
		return f'Hello {self.name}, Welcome to Blackjack!\n\nNote: You and the dealer will both start with 2 cards but you will only be able to see one of the dealers cards.\n'
	def get_value(self):
		tmp = []
		value = 0
		for piece in self.hand:
			if(piece == 'ace'):
				tmp.append['ace']
			elif(piece == 'jack' or piece == 'queen' or piece == 'king'):
				value += 10
			else:
				value += piece
		if(len(tmp)>0):
			if(value <= 11-len(tmp)):
				value = value + 11 + len(tmp) - 1
			else:
				value += len(tmp)

		return value

	def reset(self):
		Player.deck.reset_deck()
		self.hand.clear()


	def display_hand(self, num=1):
		#If num equals 1 then this method displays player 1's hand else it displays the computer's  hand
		#If num equals 2 then this method displays only the first card of the computer's hand
		if(num == 1):
			print(f'Your hand consists of {self.hand} and the value of your hand is {self.get_value()}')
		elif(num == 2):
			print(f"The computer's hand consists of {self.hand[0]} plus another card which is face down.")
		else:
			print(f"The computer's hand consists of {self.hand} and has a value of {self.get_value()}")




