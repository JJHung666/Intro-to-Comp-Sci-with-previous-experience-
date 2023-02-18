## #Homework_4_Justin_Lin.py
# Q#1:
def triangle_number(x):
	y = 0 
	for i in range(0,x+1):
		y += i
		pass
	return y
Q_1_argument = int(input("input a positive number please: "))
if Q_1_argument >= 1:	
	print(triangle_number(Q_1_argument))
	Q_1_argument = 0
	pass
else:
	while Q_1_argument < 1:
		print("the number you you entered wasn't a positive number")
		Q_1_argument = int(input("input a positive number please: "))
		continue
	print(triangle_number(Q_1_argument))
	pass

# Q#2:
def Rectangle_printer(a,b,c):
	for i in range(1,a+1):
		print(c*b)
		pass
	pass
Rectangle_printer(5,10,input('input a character please: '))

# Q#3:
def Parallelogram(a,b,c):
	for i in range(a+1,1, - 1):
		print(i * " "+ c * b)
		pass
	pass
Parallelogram(5,10,input('input a character please: '))

# Q#4:
import time

# def timer(x):
# 	minute = 0
# 	hour = 0
# 	second = 0
# 	for tenth_sec in range(1, (x*10) + 1):
# 		time.sleep(.1)
# 		if tenth_sec % 10 == 0:
# 			second += 1
# 			if second% 60 == 0:
# 				second -= 60
# 		if tenth_sec % 600 == 0:
# 			minute += 1
# 			if minute % 60 == 0:
# 				minute -= 60
# 		if tenth_sec % 36000 == 0:
# 			hour += 1
# 			if hour % 24 == 0:
# 				hour -= 24
# 		print(str(hour)+':'+str(minute)+':'+str(second)+'.'+str(tenth_sec%10))
# 	pass
# timer_1 = int(input('input timer length in seconds: '))
# # if isinstance(timer_1, int):
# 	# timer(timer_1)
# 	# pass
# timer(timer_1)

def clock_V2():
	i = 1
	time_passed = 0
	while i > 0:
		# time.sleep(.1)
		time_passed += 1
		hour = (time_passed//36000)%24
		minute = (time_passed//600)%60
		second = (time_passed//10)%60
		tenth_sec = time_passed % 10
		print(str(hour)+':'+str(minute)+':'+str(second)+'.'+str(tenth_sec))
	pass

clock_V2()