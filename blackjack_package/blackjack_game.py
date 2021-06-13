from os import system
from time import sleep
from blackjack_package.deck_class import Deck
from blackjack_package.savings_class import Savings
from blackjack_package.player_class import Player
from blackjack_package.card_class import Card

#Have to set hand2 equal to something to make the parameter optional so I just set it equal to zero
def win_check(user1, user2):
	#The variable piece represents a card in the players hand (current cards)
	value1 = user1.get_value()
	value2 = user2.get_value()
	if(value1 > 21):
		return 'p1 lost'
	elif(value2 > 21):
		return 'p2 lost'
	elif(value1 > value2):
		return 'p1 won'	
	elif(value2 > value1):
		return 'p2 won'
	else:
		return 'draw'

def game(user1, user2, saving):

	n = 1
	end_turn = False
	print('\nDealing the computers first two cards: ')
	sleep(1)
	user2.update_hand(2)
	sleep(2)
	user2.update_hand(2)
	sleep(1)
	user2.display_hand(2)
	sleep(2)
	print('\nDealing your first two cards: ')
	sleep(1)
	user1.update_hand()
	sleep(2)
	while True:
		if(n == 1):
			user1.update_hand()
			user1.display_hand()
			sleep(1)
			while True:
				option = input("\nDo you want to hit or pass ('hit' or 'pass')? ")
				if(option == 'pass'):
					end_turn = True
					break
				elif(option == 'hit'):
					break
				else:
					print("Please type the word 'hit' to hit or type the word 'pass' to pass.")
		if(end_turn):
			break
		sleep(1)
		print("The dealer is dealing you a card: ")
		user1.update_hand()
		sleep(2)
		user1.display_hand()
		sleep(1)
		if(win_check(user1, user2) == 'p1 lost'):
			print('You busted! The value of your hand is over 21.\n')
			sleep(1)
			saving.remove_money()
			break
		while True:
			option = input("\nDo you want to hit or pass ('hit' or 'pass')? ")
			if(option == 'pass'):
				end_turn = True
				break
			elif(option == 'hit'):
				n = 2
				break
			else:
				print("Please type the word 'hit' to hit or type the word 'pass' to pass.")
		if(end_turn):
			break
	if(win_check(user1, user2)!='p1 lost'):
		if(not(user2.get_value() > user1.get_value())):
			while True:
				if(n == 1):
					print("\nThe dealer is dealing the computer a card: ")
				n = 2
				sleep(1)
				user2.update_hand(2)
				sleep(2)
				if(win_check(user1, user2) == 'p2 lost'):
					user2.display_hand(3)
					print("\nYou won!\nThe computer busted; the value of the computer's hand is over 21!\n")
					sleep(1)
					saving.add_money()
					break
				elif(win_check(user1, user2) == 'p2 won'):
					user2.display_hand(3)
					print('\nYou lost! The computer got a higher valued hand.\n')
					sleep(1)
					saving.remove_money()
					break
				elif(win_check(user1, user2) == 'draw'):
					user2.display_hand(3)
					print(f'Tie game! Both you and the computer got {user2.get_value()}.')
					break
				
		else:
			print("\nYou lost! The computer had a higher valued hand.")
			user2.display_hand(3)
			print("You shouldn't have passed.\n")
			sleep(1)
			saving.remove_money()
	return saving.get_balance()

def run_game():
	#Variable to check if player ever loses all money. Set to an arbitrary value of 100
	notzerobalance = 100

	play = False
	#Asking for name
	name = input('What is your name? ')
	sleep(1)
	system('clear')

	#Creating Player objects for both the computer and the player
	user1 = Player([], name)

	user2 = Player()

	#Creating a deck for the game
	table_deck = Deck()

	#Creating a Savings object for the player to mimick the amount of cash he/she has left
	user_savings = Savings()
	
	#Introduction
	print(user1.greeting())

	#Asking player how much he/she wants to bring to the casino
	user_savings.pick_balance()

	#Checking to see if the player is ready to begin
	while True:
		play = input('\nAre you ready to play (y or n)? ')
		if(play == 'y'):
			sleep(1)
			play = True
			break
		elif(play == 'n'):
			play = False
			break
		else:
			print("Please select either 'y' (lowercase y) for yes, or 'n' (lowercase n) for no.")
			
	while play:

		system('clear')

		#Making sure the individual hands and deck is reset
		user1.reset()
		user2.reset()

		#Promting the user for the bet amount
		print(f"Balance = ${user_savings.get_balance()}")
		user_savings.bet_amount()

		#Running the game and setting the return equal to notzerobalance to make sure that the player has money in the bank
		notzerobalance = game(user1, user2, user_savings)
		
		while True and notzerobalance != 0:
			play = input(f'Your casino bank account has a balance of ${user_savings.get_balance()}.\n\nDo you want to play again (y or n)? ')
			if(play == 'y'):
				break
			elif(play == 'n'):
				play = False
				break
			else:
				print("Please select either 'y' (lowercase y) for yes, or 'n' (lowercase n) for no.")

		if(notzerobalance == 0):
			sleep(1)
			print("\nSorry you can't play anymore, you ran out of money.\nCome back another time!\n")
			break
	if(notzerobalance != 0):
		print('\nBye, I hope you had fun!\n')





