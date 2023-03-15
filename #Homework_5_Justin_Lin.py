# Homework_5_Justin_Lin.py
# Q#1
big_total = 0
maximum_share = 0
def div_w_remainder(dividend,divisor):
	whole = dividend//divisor
	remainder = dividend%divisor
	return whole,remainder

def share_items(number_of_things, number_of_people):
	global big_total
	global maximum_share
	result = div_w_remainder(number_of_things, number_of_people)
	big_total += number_of_things
	maximum_share += result[0]
	if result[1] > 0:
		maximum_share += 1
	# print(big_total, maximum_share)

def question_1():
	share_items(10, 4)
	share_items(20, 3)
	share_items(14, 7)
	print(big_total, maximum_share)
question_1()


# I combined Q#2 & 3
from turtle import *
import random
arm_position = 0
leg_position = 0
size = 0
def head(x):
	circle(x)
def neck(x):
	right(90)
	fd(x)
def left_arm(x):
	global arm_position
	arm_position = random.randrange(65,115)
	right(arm_position)
	fd(x)
	backward(x)
def right_arm(x):
	global arm_position
	left(arm_position*2)
	fd(x)
def torso(x):
	global arm_position
	backward(x)
	right(arm_position)
	fd(x)
def left_leg(x):
	global leg_position
	leg_position = random.randrange(25,65)
	left(leg_position)
	fd(x)
	backward(x)
def right_leg(x):
	global leg_position
	right(leg_position*2)
	fd(x)
def Body_Assemble():
	global size
	size = random.randrange(70,110)
	begin_fill()
	head(size)
	clr = random.randrange(1,3)
	if clr == 1:
		color("blue", "red")
	elif clr == 2:
		color("red", "yellow")
	else:
		color("yellow","blue")
	end_fill()
	neck(size)
	left_arm(size)
	right_arm(size)
	torso(size)
	left_leg(size)
	right_leg(size)
	reset()
for i in range(5):
	Body_Assemble()