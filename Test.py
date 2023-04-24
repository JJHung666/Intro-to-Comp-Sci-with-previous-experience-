# Test.py
import random
def roll(faces):
		percentage = 100
		side_list = list(range(1, faces+1))
		# print(side_list)
		weighted_list = []
		for x in range(0, faces-1):
			temporary_weight = 100//faces + random.randint(-1*(100//faces)//faces, (100//faces)//faces)
			weighted_list.append(temporary_weight)
			percentage = percentage - temporary_weight
		weighted_list.append(percentage)
		print(sum(weighted_list))
		# return random.choices(side_list, weights = weighted_list, k = 1)
# print(roll(6))
roll(6)