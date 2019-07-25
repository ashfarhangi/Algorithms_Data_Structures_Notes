# why are we using self and all that in machine learning?
# There is no use of that. All of the machine learning problems can be solved as a data engineering problems

# Problem 1: Tokenize a dataset
import os
addresses = [51234,3413245,412341235,132231344]
def tokenize(arg1):
	tokenized_address = [[],
						[]]
	i = 0
	for item in arg1:
		tokenized_address[0].append(item)
		item = i 
		tokenized_address[1].append(item)
		i+=1
		tokenized_address
	with open("token.txt",'w') as f:
		for item in str(tokenized_address):
			f.write(item)
	print(tokenized_address)
	return tokenized_address
tokenize(addresses)
def de_tokenize(arg1):
	new_list = []
	with open("token.txt",'r') as f:
		for item in f:
			new_list.append(f)
	print(new_list)
	return new_list

de_tokenize(addresses)