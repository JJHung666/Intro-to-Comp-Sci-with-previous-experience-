# Homework_10_Justin_Lin.py
# Question #1
# Make a subclass of turtle that draws a rainbow structure
from turtle import *
import math
import random

class Rainbow_Turtle(Turtle):
	global rainbow_list
	rainbow_list = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]	
	def __init__(self):
		Turtle.__init__(self)
		self.pu()
		self.setpos(-50,-50)
		self.pd()
		bgcolor("black")
	def Polygon(self, distance, sides):
		for x in range(sides):
			for y in range(distance//5):
				self.forward(y)
				self.pencolor(random.choice(rainbow_list))
			self.left(360/sides)

def test_turtle():
	polygon_1 = Rainbow_Turtle()
	polygon_1.speed(0)
	for x in range(3, 8):
		polygon_1.Polygon(100, x)
	done()
test_turtle()

# Question #2
# Subclass for weighted die
class Weighted_Die():
	# number_of_rolls = 0
	def __init__(self, sides):
		self.faces = sides
		# Weighted_Die.number_of_rolls += 1
	def roll(self):
		percentage = 100
		side_list = list(range(1, self.faces+1))
		weighted_list = []
		for x in range(0, self.faces-1):
			temporary_weight = 100//self.faces + random.randint(-1*(100//self.faces)//self.faces, (100//self.faces)//self.faces)
			weighted_list.append(temporary_weight)
			percentage = percentage - temporary_weight
		weighted_list.append(percentage)
		return random.choices(side_list, weights = weighted_list, k = 1)

test_die = Weighted_Die(6)
print('Testing Weighted Die (20 rolls)')
for num in range(20):
	print(test_die.roll())

# Question #3

class Die:
	side = 0
	def __init__(self):
		# self.roll_history = []
		pass

	# def __str__(self):
	# 	return f"Last roll: {self.roll_history[-1]}"

	def roll(self):
		value = random.randint(1,self.side)
		# self.roll_history.append(value)
		# return self.roll_history
		return value
	
	@classmethod
	def Set_Sides(cls, amount):
		cls.side = amount

def game():
	player = Die()
	Computer = Die()
	player_dict = {}
	Computer_dict = {}
	for i in range(1, 11):
		Die.Set_Sides(i)
		# print(player.roll())
		player_dict[i] = player.roll()
		Computer_dict[i] = Computer.roll()
	print("This is Boom!")
	player_score = 0
	Computer_score = 0
	while len(player_dict) >= 1:
		y = list(Computer_dict.keys())
		Computer_roll = Computer_dict.pop(y[random.randrange(0,len(y))])
		print("The Computer has rolled a " + str(Computer_roll))
		x = list(player_dict.keys())
		print(x)
		try:
			choice = int(input("Choose a die by number. Currently you have dice with the following numbers of sides."))
			player_roll = player_dict.pop(choice)
			print("You have just rolled a " + str(player_roll))
			if player_roll > Computer_roll:
				player_score += player_roll
			elif Computer_roll > player_roll:
				Computer_score += Computer_roll
			else:
				pass
		except:
			print("your choice was unacceptable, please try again.")
	print("This is your score: " + str(player_score))
	print("This is the computer's score: " + str(Computer_score))
	if player_score > Computer_score:
		print("you've won")
	elif player_score < Computer_score:
		print("you've lost")
	else:
		print("You've tied")
		
game()