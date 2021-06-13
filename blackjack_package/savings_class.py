from time import sleep
class Savings:

	def __init__(self, balance=1000, bet=1000):
		self.balance = balance
		self.bet = bet

	def pick_balance(self):
		while True:
			try:
				newbal = (int)(input('How much money do you want start with in your casino bank account (greater than 0)? '))
				if(newbal <= 0):
					raise ValueError('Error.')
			except:
				print("Sorry that didn't work, please select a valid non-decimal number greater than 0. ")
			else:
				sleep(1)
				print(f'Money validated. An account with ${newbal} has been created under your name.')
				self.balance = newbal
				break

	def get_balance(self):
		return self.balance

	def remove_money(self):
		print(f"${self.bet} has been deducted from your casino bank account.")
		self.balance -= self.bet

	def add_money(self):
		print(f"${self.bet} has been added to your casino bank account.")
		self.balance += self.bet

	def bet_amount(self):
		while True:
			try:
				amt = (int)(input('How much money do you want to bet? '))
				if(amt <= 0 or amt > self.balance):
					raise ValueError('Error.')
			except:
				print("Please select a valid amount (non-decimal integer number) which is less than your casino bank account's current balance.")
			else:
				sleep(1)
				print(f'${amt} was successfully added to the pot.')
				self.bet = amt
				break

