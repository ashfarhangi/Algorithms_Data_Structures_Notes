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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
def tele_market_detect():
	tele_numbers = []
	out_going = []
	for item in calls:
		out_going.append(item[1])
	for i in range(len(calls)):
		if (calls[i][0] not in out_going):
			tele_numbers.append(calls[i][0])
			tele_numbers1=set(tele_numbers)
	print(len(tele_numbers1))	
	for i in range(len(tele_numbers1)):
		if(tele_numbers[i] in texts[i][0]):
			tele_numbers1.remove(tele_numbers1[i])
		if(tele_numbers[i] in texts[i][1]):
			tele_numbers1.remove(tele_numbers1[i])	
	print(len(tele_numbers1))
	print("These numbers could be telemarketers: ")
	for item in tele_numbers1:
		print("{}\n".format(item))
	return 
tele_market_detect()