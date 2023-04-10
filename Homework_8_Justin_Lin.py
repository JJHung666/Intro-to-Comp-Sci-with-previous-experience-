# Homework_8_Justin_Lin.py
# Question #1
def Number_Queries(How_many, Low, High):
	Accumulated_list = []
	counter = 0
	print("The low end of the range is: " + str(Low) + "\nThe high end of the range is: " + str(High))
	while How_many > counter:
		pick = input("please pick a number from "+str(Low)+" to "+str(High)+" ")
		picked = pick.isnumeric()
		if picked:
			pick = int(pick)
		else:
			print("That number was no good. Try again")
		if isinstance(pick, int) and pick <= High and pick >= Low:
			Accumulated_list.append(pick)
			counter += 1
		else:
			print("choose an acceptable number")
	return(Accumulated_list)
reps = int(input("How many numbers? "))
small = int(input("enter the low of the range "))
big = int(input("enter the high of the range" ))
if small < big:
	print(Number_Queries(reps, small, big))
elif big < small:
	print(Number_Queries(reps, big, small))
else:
	print("you did something wrong")

# Question #2
import os
f = open("/Users/jjhung666/Documents/GitHub/Intro-to-Comp-Sci-with-previous-experience-/Wiki.txt", "r")
# f = open("Wiki.txt", "r")
# vowel_list = ['a','e','i','o','u']
# vowel_counter = 0
a_counter = 0
e_counter = 0
i_counter = 0
o_counter = 0
u_counter = 0
for character in f.read():
	# if character.lower() in vowel_list:
		# vowel_counter += 1
	if character.lower() == "a":
		a_counter += 1
	elif character.lower() == "e":
		e_counter += 1
	elif character.lower() == "i":
		i_counter += 1
	elif character.lower() == "o":
		o_counter += 1
	elif character.lower() == "u":
		u_counter += 1
# print("\nThere are " + str(vowel_counter) + " Vowels available in the File")
f.close()
file = open("Wiki.vowel_profile", "w")
file.write("this is a vowel profile file.\n The A Frequency is: "+ str(a_counter) +" \n The E Frequency is: "+ str(e_counter) +" \n The I Frequency is: "+ str(i_counter) +" \n The O Frequency is: "+ str(o_counter) +" \n The U Frequency is: "+ str(u_counter))
# print(file.read()) Can't read file because it isn't a txt file

# Question #3
import os
# filehandle = open("hw7.tsv", "r")
with open('hw7.tsv', 'r') as filehandle:
	filelist = filehandle.readlines()
print(filelist)
baseball_team_scores = []
for x in filelist:
	item = x.replace('\n','')
	item = item.split("\t")
	for y in range(1, len(item)):
		try:
			item[y] = int(item[y])
		except:
			pass
	# item[1:-1] = int(item[1:-1])
	baseball_team_scores.append(item)

# print(baseball_team_scores)

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

# Question #4
import os
def collect_and_update_reviews(Max_Star, File_Name):
	output = []
	with open(File_Name, "r") as fileforQ4:
		for x in fileforQ4:
			line = x.strip(os.linesep)
			tsv_list = line.split('\t')
			output.append(tsv_list)
	print(output)
	Q4_questioneer = output[0][1:]
	questioneer_result = [(len(output))]
	# print(questioneer_result)
	i = 0
	while i < (len(output[0])-1):
		try:
			result = float(input("How many stars from 1 to " + str(Max_Star) + " would you give to " + Q4_questioneer[i] + "? "))
		except:
			pass
		if result >=1 and result <= Max_Star:
			i += 1
			questioneer_result.append(result)
		else:
			print("the answer you gave was not satisfactory")
		# filelist = fileforQ4.readlines()
	# print(filelist)
	# print(questioneer_result)
	for num in range(1, len(output)):
		for i in range(len(output[num])):
			output[num][i] = float(output[num][i])
	output.append(questioneer_result)
	# print(output)
	global uncle_av
	global bob_av
	global Kashi_av
	global grape_av
	global Ez_av

	uncle_av = 0
	bob_av = 0
	Kashi_av = 0
	grape_av = 0
	Ez_av = 0
	for x in range(1, len(output[0])):
		for y in range(1, len(output)):
			if x == 1:
				uncle_av += output[y][x]
			elif x == 2:
				bob_av += output[y][x]
			elif x == 3:
				Kashi_av += output[y][x]
			elif x == 4:
				grape_av += output[y][x]
			elif x == 5:
				Ez_av += output[y][x]

	uncle_av /= 7
	bob_av /= 7
	Kashi_av /= 7
	grape_av /= 7
	Ez_av /= 7

loop_check = True
while loop_check:
	choice = input("Would you like to add an additonal set of reviews? Y/N ")
	if choice.lower() == "y":
		collect_and_update_reviews(5,"/Users/jjhung666/Documents/GitHub/Intro-to-Comp-Sci-with-previous-experience-/healthfood_cereals.tsv")
	else:
		print("this is the average rating of uncle: " + str(round(uncle_av, 2)))
		print("this is the average rating of bob: " + str(round(bob_av, 2)))
		print("this is the average rating of Kashi: " + str(round(Kashi_av, 2)))
		print("this is the average rating of grape: " + str(round(grape_av, 2)))
		print("this is the average rating of Ez: " + str(round(Ez_av, 2)))
		loop_check = False	

