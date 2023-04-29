# Homework_11_Justin_Lin.py
# Question #1
# Write a recursion function that calculates traingle numbers
def triangle(x):
	if x ==  1 :
		return x
	else:
		return x + triangle(x-1)

print(triangle(5))

# Question #2
def Question_2():
	Question2 = input("Are we there yet? ")
	if Question2.lower() == "yes":
		return(Question2)
	else:
		return Question_2()
Question_2()

# Question #3
def list_sorter(list3):
	if len(list3) == 2:
		item1 = list3[0]
		item2 = list3[1]
		if item1 < item2:
			return ([item1,item2])
		else:
			return ([item2,item1])
	elif len(list3) == 1 or len(list3) == 0:
		return list3
	else:
		pivot = list3[0]
		list1 = []
		list2 = []
		for i in range(1, len(list3)):
			if list3[i] < list3[0]:
				list1.append(list3[i])
			else:
				list2.append(list3[i])
		newlist = list_sorter(list1)
		newlist.append(pivot)
		newlist.extend(list_sorter(list2))
		return newlist
print(list_sorter([35, 42, 39, 7, 49, 46, 33, 43, 28, 25]))

# Question #4
from turtle import *
Turtle()
Screen()
bgcolor("black")
setpos(0,0)
color_changer = 1
speed(speed = 0)
def turtle_spiral(length):
	question_4_colors = ["yellow", "blue"]
	global color_changer
	color_changer += 1
	if length > 1:
		pencolor(question_4_colors[color_changer%2])
		forward(length)
		left(90)
		return turtle_spiral(length-1)
	else:
		pass
turtle_spiral(100)
done()