#Homework_7_Justin_Lin.py
#Q#1
#data format [team_name, wins, losses, ties]
baseball_team_scores = [['Mets',10,5,5], ['Yankees',11,2,2], ['Bears',7,15,0], ['Senators',5,30,1], ['Clowns',10,50,1]]

def sort_baseball_scores(baseball_team_score):
	team_name, wins, losses, ties = baseball_team_score
	score = (wins + ties/2)/(wins+losses+ties)
	return(score)

def Sorting_scores(baseball_team_score):
	list_to_sort = []
	for i in baseball_team_score:
		Sorted_List = [sort_baseball_scores(i)]
		Sorted_List.extend(i)
		list_to_sort.append(Sorted_List)
	list_to_sort.sort()
	return(list_to_sort)

# print(Sorting_scores(baseball_team_scores))
#I commented the line above, because the results were ugly looking
for x in (Sorting_scores(baseball_team_scores)):
	print(x[1:])

#Q#2
import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("yellow")

def BiPartite_Graph(Coordinate_1, Coordinate_2):
	for x in range(len(Coordinate_1)):
		for i in range(len(Coordinate_2)):
			t.pu()
			t.setposition(Coordinate_1[x])
			t.pd()
			t.setposition(Coordinate_2[i])

coord_list_1 = [[-200,200],[-200,90],[-50,-20]]
coord_list_2 = [[50,200],[50,170],[300,90],[50,30],[50,0],[50,-13],[50,-73]]
BiPartite_Graph(coord_list_1, coord_list_2)

turtle.done()

#Q#3
from random import *
deck_of_cards = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K','A',2,3,4,5,6,7,8,9,10,'J','Q','K']

def Draw_Card():
	global deck_of_cards
	Drawn = deck_of_cards.pop(randrange(0,len(deck_of_cards)))
	return(Drawn)
#A=1, J,Q,K = 10
# print(Draw_Card())
# print(len(deck_of_cards))
Player_hand = []
Program_hand = []
def player_draw():
	global Player_hand
	Player_hand.append(Draw_Card())
def Program_draw():
	global Program_hand
	Program_hand.append(Draw_Card())
def start():
	#player and program both get 2 cards
	for i in range(2):
		Program_draw()
		player_draw()
start()
game_state = True
program_state = True
Player_list = []
Program_list = []
while game_state:
	Player_list = []
	for card in range(len(Player_hand)):
		appearance = False
		if Player_hand[card] == 'A':
			Player_list.append(1)
			appearance = True
		elif Player_hand[card] == 'J':
			Player_list.append(10)
		elif Player_hand[card] == 'Q':
			Player_list.append(10)
		elif Player_hand[card] == 'K':
			Player_list.append(10)
		else:
			Player_list.append(Player_hand[card])
		if appearance and sum(Player_list) <= 11:
			Player_list[card] = 11
	print("this is currently the value of your hand: "+ str(sum(Player_list)))
	print("your current hand:")
	for hand in Player_hand:
		print(hand)
	if (sum(Player_list) < 21):
		for hand in Player_hand:
			for hand2 in Player_hand:
				if hand == "A" and (hand2 == 10 or hand2 == 'J' or hand2 == 'Q' or hand2 == 'K'):
					game_state = False
		if (input("please input Y if you want to draw an additional card: ").upper() == 'Y'):
			player_draw()
		else:
			print("you have decided to not draw and end the match")
			game_state = False
	else:
		break
while program_state:
	Program_list = []	
	for card in range(len(Program_hand)):
		appearance = False
		if Program_hand[card] == 'A':
			Program_list.append(1)
			appearance = True
		elif Program_hand[card] == 'J':
			Program_list.append(10)
		elif Program_hand[card] == 'Q':
			Program_list.append(10)
		elif Program_hand[card] == 'K':
			Program_list.append(10)
		else:
			Program_list.append(Program_hand[card])
		if appearance and sum(Program_list) <= 11:
			Program_list[card] = 11	
	print("this is currently the value of the computer's hand: "+ str(sum(Program_list)))
	print("Program's current hand:")
	for hand in Program_hand:
		print(hand)
	if (sum(Program_list) < 21):
		for hand in Program_hand:
			for hand2 in Program_hand:
				if hand == "A" and (hand2 == 10 or hand2 == 'J' or hand2 == 'Q' or hand2 == 'K'):
					program_state = False
		if sum(Program_list) <= 16:
			Program_draw()
		else:
			program_state = False
	else:
		break
print("player score: " + str(sum(Player_list)))
print("computer score: " + str(sum(Program_list)))
# Lose Condition: The dealer has Black Jack (to be defined) or The player's hand > 21 or there is a tie
# Win Condition: The player has Black Jack or The dealer's hand > 21 or The player's hand > the dealer's hand
if sum(Player_list) <= 21 and sum(Program_list) <= 21:
	if sum(Player_list) > sum(Program_list):
		print("Player has beaten Computer")
	elif sum(Player_list) < sum(Program_list):
		print("Computer has beaten Player")
	elif sum(Player_list) == sum(Program_list):
		print("It's a tie")
elif sum(Player_list) > 22 and sum(Program_list) <= 21:
	print("Player has lost")
elif sum(Player_list) <= 22 and sum(Program_list) > 22:
	print("Computer has lost")
else:
	print("Both have lost")