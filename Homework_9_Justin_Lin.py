# Homework_9_Justin_Lin.py
# Question #1
def word_count(txt):
	word_bank = {}
	words = txt.split()
	# words = txt.strip(",.!?\'”")
	New_Text_File = ""

	for word in words:
		word = word.strip(",.!?\'”")
		if word in word_bank:
			word_bank[word] += 1
		else:
			word_bank[word] = 1

	for key in word_bank.keys():
		New_Text_File += (str(key) +"\t"+ str(word_bank.get(key)) +"\n")

	return New_Text_File
file_for_Q1 = open("Wiki.txt",'r')
print(word_count(file_for_Q1.read()))

# Question #2
def Holiday_Dates(Holiday_str):
	DateDict = {
	"Christmas": '12/25/2021',
	"Easter": '4/4/2021',
	"Thanksgiving": '11/25/2021',
	"Halloween": '10/31/2021',
	"MLK": '1/18/2021',
	"Kwanzaa": '12/26/2021',
	"Hanukkah": '11/28/2021',
	"Ramadan": '4/12/2021',
	}
	new_line = ""
	for word in Holiday_str.split(" "):
		if word in DateDict:
			new_line += DateDict[word]
		else:
			new_line += word + " "
	return (new_line)

# file_for_Q2 = open("",'r')
test_string = "I wish you a merry Christmas"
print(Holiday_Dates(test_string))

# Question #3

def Phone_Book_updater(filename):
	file = open(filename, 'r')
	filelist = file.readlines()
	this_dict = {}
	for item in filelist:
		templist = item.split()
		if templist[0] in this_dict:
			this_dict[templist[0]].append(templist[1]) 
		else:
			this_dict[templist[0]] = [templist[1]]
	choice = input("would you like to add a new number to the phone book? Yes or No? ")
	if choice.lower() == "yes":
		add_name = input("please input the name of the number holder: ")
		add_number = input("please input the phone number: ")
		if add_name in this_dict:
			this_dict[add_name].append(add_number)
		else:
			this_dict[add_name] = [add_number]
	else:
		pass
	print(this_dict)

# file_for_Q3 = input("please enter the pathname of the file: ")
file_for_Q3 = "/Users/jjhung666/Documents/GitHub/Intro-to-Comp-Sci-with-previous-experience-/2nd_phone_book.tsv"
Phone_Book_updater(file_for_Q3)

# Question #4
def reverse_Phone_book(infile, outfile):
	file = open(infile, 'r')
	filelist = file.readlines()
	this_dict = {}
	this_list = []
	for item in filelist:
		templist = item.split()
		if templist[1] in this_dict:
			this_dict[templist[1]].append(templist[0]) 
		else:
			this_dict[templist[1]] = [templist[0]]
	this_list = list(this_dict.keys())
	this_list.sort()
	outfile = open(outfile, "w")
	Q4_string = ""
	for phone_number in this_list:
		for name in this_dict[phone_number]:
			Q4_string += phone_number +"\t"+ name + "\n"
		
	outfile.write(Q4_string)


reverse_Phone_book("/Users/jjhung666/Documents/GitHub/Intro-to-Comp-Sci-with-previous-experience-/2nd_phone_book.tsv", "Reverse_Phone_Book")
