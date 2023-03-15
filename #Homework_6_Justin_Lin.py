# Homework_6_Justin_Lin.py
# Q#1
def secret_code(arg):
	thislist = []
	for i in arg:
		thislist.append(ord(i))
	print('[', ' '.join(str(x) for x in thislist), ']')

secret_code(input("please enter a random string"))

# Q#2
def make_english_verb_ing(string):
	if (string[-1] in ['a','e','i','o','u'] and string[-2] in ['a','e','i','o','u']) or ((string[-1] not in ['a','e','i','o','u']) and (string[-2] in ['a','e','i','o','u']) and (string[-3] in ['a','e','i','o','u'])) or (string[-1] == 'y') or (string[-1] not in ['a','e','i','o','u'] and string[-2] not in ['a','e','i','o','u'] and string[-3] in ['a','e','i','o','u']):
		return (string + 'ing')
	elif string[-1] == 'e' and string[-2] in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'z']:
		return (string[:-1] + 'ing')
	elif ((string[-2] in ['a','e','i','o','u']) and (string[-1] in ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'z']) and (string[-3] not in ['a','e','i','o','u'])):
		return (string + string[-1] + 'ing')

print(make_english_verb_ing(input("insert word: ")))

# Q#3: PT.1
from number_program_input import *
Inputted_number = input("insert a word number please: ")
splitted = Inputted_number.lower().split()
output = list(map(word_to_number, splitted))
print(output)
output2 = [output[0]]
for i in range(1, len(output)):
	if output[i] < 1000:
		if output[i-1] < output[i]:
			output2[-1] *= output[i]
		else:
			output2.append(output[i])
	else:
		output2.append(output[i])
print(output2)
output3 = [output2[0]]
for i in range(1, len(output2)):
	if output2[i] < 1000:
		if output2[i-1] < 1000 and output2[i-1] > output2[i]:
			output3[-1] += output2[i]
		else:
			output3.append(output2[i])
	else:
		output3.append(output2[i])
print(output3)
output4 = [output3[0]]
for i in range(1, len(output3)):
	if output3[i-1] < output3[i]:
		output4[-1] *= output3[i]
	else:
		output4.append(output3[i])
print(output4)
print(sum(output4))