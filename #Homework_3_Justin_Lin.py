# # #Homework_3_Justin_Lin.py
# # Part 1 Q#1
# def Question_1(number_1):
# 	if number_1 == 0:
# 		print("zero")
# 		pass
# 	elif (number_1 % 2) == 0:
# 		print("even")
# 		if (number_1 % 3) == 0 :
# 			print("divisible by three")
# 		pass
# 	elif (number_1 % 2) != 0:
# 		print("odd")
# 		if (number_1 % 3) == 0 :
# 			print("divisible by three")
# 			pass
# 		pass
# 	pass
# Question_1(int(input("enter a whole number: ")))


# # Part 1 Q#2
# def Question_2(number_2):
# 	if (number_2 % 2) == 0 and (number_2 % 3) > 0:
# 		print(str(number_2) + " is even and not divisble by 3")
# 		return True
# 	elif (number_2 % 2) != 0 and (number_2 % 3) == 0:
# 		print(str(number_2) + " is odd and divisble by 3")
# 		return True
# 	else:
# 		print("Does not satisfy conditions 1 and 2")
# 		return False
# Question_2(int(input("enter a whole number: ")))


# # Part 1 Q#3
# def Generate_Truth_Row(p, q):
# 	block_1 = str(p)
# 	block_2 = str(q)
# 	block_3 = str((p == q))
# 	block_4 = str((p != q))
# 	block_5 = str((p and q))
# 	block_6 = str((p or q))
# 	print(block_1 + "\t" + block_2 + "\t " + block_3 + "\t " + block_4 + "\t " + block_5 + "\t " + block_6)
# 	pass

# def Generate_Truth_Table():
# 	#First Row
# 	print("p \t q \t p==q \t p!=q \t p & q \t p or q")
# 	Generate_Truth_Row(False, False)
# 	Generate_Truth_Row(False, True)
# 	Generate_Truth_Row(True, False)
# 	Generate_Truth_Row(True, True)
# 	pass
# Generate_Truth_Table()


# # Part 2 Q#1 & #2 comment section
# '''
# Interactive game Based: Build a CAC for an RPG
# System:
# Character Name: Input
# Base Stats (varies based on class): Str, HP, MP, Agi, Def, & Rec
# Stat points: 0
# Base Lvl: 1
# Lvl = Base Lvl + x
# stat point = lvl * 6
# def Stat allocation():
# EXP = 100 + lvl(*100)
# Exp to next lvl = EXP - EXP gained
# Exp Gained = monster_lvl*15
# Choose Class: Knight, Mage, Assasin
# Class Perks: Berserker, self buff, Critical Stab
# Goal: climb to the top floor (total 5 floors)
# each floor have mobs that spawn infinitely, and a boss monster

# Story:
# choose character class
# 	Choose to fight mobs?
# 	Choose to fight floor boss?
# 	regular hit or perk ability
# stay or move to next floor?
# when at floor 5, congratulations you have finished the decision tree game

# # Fighting mechanic:
# # The one with higher agility goes first
# # dmg = str - def
# # ability_berserker = str + mp/2 for 2 turns
# # ability_self_buff = all stats + mp/6
# # ability_Criticcal_stab = for next turn, dmg * mp
# # remaining_hp = hp
# # remaining_hp = remaining_hp - dmg


# Coding Logic:
# Character Set_up:
# First allow user to choose class, and explain how the class perks works
# Give them a status window, and allow them to allocate points to their stats
# Then ask whether they would like to fight the mobs or the floor boss
# # Code the fighting mechanic
# # when enemy is killed, exp is gained.
# # when lvled up, ask for stat allocation again
# # after a battle, repeat earlier question (fight mob or floor boss)
# # when defeating floor boss, ask to quit game or move on to the next floor.
# # repeat this until game is finished
# '''

# Part 2 Q#3: Coding portion
# the variables for lines 110-117 are the variables that can change depending on the user's input
stat_points = 0
lvl = 1
Strength = 3
Health_Points = 3
Mana_Points = 3
Agility = 3
Defense = 3
Recovery = 3
# The Character_setup function will be the function responsiple for calling the other functions
def Character_setup():
	Character_name = input("Enter your character's name: ")
	print("Welcome to Justin's Priliminary RPG, " + Character_name)
	Class = str(Chosen_Class())
	# I'm using a global variable to allow multiple separate functions to use the same variable
	global stat_points
	# The if statement below is for both input validation as well to progress the decision tree.
	if Class.capitalize() == "Knight" or Class.capitalize() == "Mage" or Class.capitalize() == "Assassin":
		print("you have chosen to be a " + Class.capitalize())
		pass
	else:
		# the while loop will continue forever until the user input is validated
		while Class.capitalize() != "Knight" and Class.capitalize() != "Mage" and Class.capitalize() != "Assassin":
			print("the class you chose is incorrect or illegible, so please choose again")
			# this is recalling the Chosen_Class() Function. This should satisfy the "reusing" parts of the decision tree goal.
			Class = str(Chosen_Class())
			continue
		print("you have chosen to be a " + Class.capitalize())
		pass
	# The 3 if/elif statements below are for input validation, as well as showing that different choices move you along different branches on the decision tree.
	if Class.capitalize() == "Knight":
		global Strength
		Strength += 1
		print("All players have 3 stat points for all basic stats, and as a " + Class.capitalize() + " you have been awarded a free stat point into your Strength stat")
		pass
	elif Class.capitalize() == "Mage":
		global Mana_Points
		Mana_Points += 1
		print("All players have 3 stat points for all basic stats, and as a " + Class.capitalize() + " you have been awarded a free stat point into your MP stat")
		pass
	elif Class.capitalize() == "Assassin":
		global Agility
		Agility += 1
		print("All players have 3 stat points for all basic stats, and as a " + Class.capitalize() + " you have been awarded a free stat point into your Agility stat")
		pass
	print("You are currently lvl 1, You have been rewarded 6 stat points. Please allocate your stats to either of the following: Strength, Health points, Mana points, Agility, Defense, and Recovery")
	stat_points = 6
	allocate_stats()
	pass
def Chosen_Class():
	Choose_Class = input("Please choose a character class. There are 3 available choices: Knight, Mage, or Assassin: ")
	return Choose_Class
def allocate_stats():
	# Same reason as above, the global variables allow me to use the same variables across other functions.
	global stat_points
	global Strength
	global Health_Points
	global Mana_Points
	global Agility
	global Defense
	global Recovery
	while stat_points > 0:
		# as the variable name indicates, stat_placeholder is the variable that is responsible for breaking the while loop once the conditions have been met.
		stat_placeholder = 0
		print("you currently have: " + str(stat_points) + " stat points left")
		print("your current stats are shown below")
		print("your current Strength stat is " + str(Strength)+ "\nyour current Health Points stat is " + str(Health_Points)+ "\nyour current Mana Points stat is " + str(Mana_Points)+ "\nyour current Agility stat is " + str(Agility)+ "\nyour current Defense stat is " + str(Defense)+ "\nyour current Recovery stat is " + str(Recovery))
		Allocation_input = input("Which stat would you like to add points to? ")
		if Allocation_input.capitalize() == "Strength" or Allocation_input.capitalize() == "Str":
			stat_placeholder = int(input("How many points will you add to Strength? "))
			if stat_placeholder <= stat_points:
				Strength += stat_placeholder
				stat_points -= stat_placeholder
				pass
			else:
				print("you have entered a number greater than your allotted stat points")
				pass
			pass
		elif Allocation_input.capitalize() == "Health points" or Allocation_input.capitalize() == "Hp":
			stat_placeholder = int(input("How many points will you add to HP? "))
			if stat_placeholder <= stat_points:
				Health_Points += stat_placeholder
				stat_points -= stat_placeholder
				pass
			else:
				print("you have entered a number greater than your allotted stat points")
				pass
			pass
		elif Allocation_input.capitalize() == "Mana points" or Allocation_input.capitalize() == "Mp":
			stat_placeholder = int(input("How many points will you add to MP? "))
			if stat_placeholder <= stat_points:
				Mana_Points += stat_placeholder
				stat_points -= stat_placeholder
				pass
			else:
				print("you have entered a number greater than your allotted stat points")
				pass
			pass
		elif Allocation_input.capitalize() == "Agility" or Allocation_input.capitalize() == "Agi":
			stat_placeholder = int(input("How many points will you add to Agility? "))
			if stat_placeholder <= stat_points:
				Agility += stat_placeholder
				stat_points -= stat_placeholder
				pass
			else:
				print("you have entered a number greater than your allotted stat points")
				pass
			pass
		elif Allocation_input.capitalize() == "Defense" or Allocation_input.capitalize() == "Def":
			stat_placeholder = int(input("How many points will you add to Defense? "))
			if stat_placeholder <= stat_points:
				Defense += stat_placeholder
				stat_points -= stat_placeholder
				pass
			else:
				print("you have entered a number greater than your allotted stat points")
				pass
			pass
		elif Allocation_input.capitalize() == "Recovery" or Allocation_input.capitalize() == "Rec":
			stat_placeholder = int(input("How many points will you add to Recovery? "))
			if stat_placeholder <= stat_points:
				Recovery += stat_placeholder
				stat_points -= stat_placeholder
				pass
			else:
				print("you have entered a number greater than your allotted stat points")
				pass
			pass
		else:
			print("It seems that the stat name you have entered it not recognized, please enter them again in the correct format")
			pass
		continue
	print("your current stats are shown below")
	print("your current Strength stat is " + str(Strength))
	print("your current Health Points stat is " + str(Health_Points))
	print("your current Mana Points stat is " + str(Mana_Points))
	print("your current Agility stat is " + str(Agility))
	print("your current Defense stat is " + str(Defense))
	print("your current Recovery stat is " + str(Recovery))
	pass
Character_setup()