"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def split():
	
def unique_num():
	total_num =[]
	for item in texts:
		total_num.append(str(item))
	print(len(total_num))
	for item in calls:
		total_num.append(str(item))
	print(total_num)
	unique_numbers_count = set(total_num)
	print("total entry:",len(total_num),"unique numbers: ",len(unique_numbers_count))
	return unique_numbers_count
unique_num()

"""Feedbacks"""
# def once_call_text_numbers(text,call):
# 	temp=[]
# 	counter = 0
# 	for i in range(len(text)):
# 		temp.append(text[i][0])
# 		temp.append(text[i][1])
# 	for j in range(len(calls)):
# 		temp.append(calls[j][0])
# 		temp.append(calls[j][1])
# 	for i in range(len(temp)):
# 		arg1 = temp.count(temp[i])
# 		if (arg1==1):
# 			counter +=1
# 	print(len(temp))
# 	print("there are ",counter,"once called, text numbers in dataset")
# once_call_text_numbers(texts,calls)
#Not efficient
# def unique_addresses():
# 	with open("data/block_list.txt",'r') as f:
# 		block_addresses=list(f)
# 	unique_list=[]
# 	for address in block_addresses:
# 		if (block_addresses.count(address)==1):
# 			unique_list.append(address)
# 	print(len(address))
# Not efficient


#Slow
# def unique_addresses():
# 	with open("data/block_list.txt",'r') as f:
# 		block_addresses=list(f)
# 	unique_list=[]
# 	for address in block_addresses:
# 		if address not in unique_list:
# 			unique_list.append(address)
# 	print(len(address))
# unique_addresses()

# def unique_numbers(text,call):
# 	temp=[]
# 	counter = 0
# 	for i in range(len(text)):
# 		temp.append(text[i][0])
# 		temp.append(text[i][1])
# 	for j in range(len(calls)):
# 		temp.append(calls[j][0])
# 		temp.append(calls[j][1])
# 	while(len(temp)>0):
# 		i=0
# 		idx = 0
# 		freeze = temp[i]
# 		while (temp.count(freeze)!=0):
# 			idx = temp.index(freeze)
# 			del temp[idx]
# 		counter +=1
# 		i+=1
# 		print(counter)
# 	print(len(temp))
# 	print("there are ",counter," unique text and call numbers in dataset")	
# unique_numbers(texts,calls)

# DONE