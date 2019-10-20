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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
def list_area_codes():
	area_list = []
	for item in calls:
		# mobile
		if (item[0][0]=="7"or item[0][0]=="8" or item[0][0]=="9" ):
			area_list.append(item[0][0:4])
		# Telemarketing
		if (item[0][0:3]=="140" ):
			area_list.append(item[0][0:3])
			# Fixed
		if (item[0][0]=="("):
			if(item[0][4]==")"):
				area_list.append(item[0][1:4])
			if(item[0][5]==")"):
				area_list.append(item[0][1:5])
		#
	print("The numbers called by people in Bangalore have codes: ")		
	for item in set(area_list):
		print("{}\n".format(item))
	print("List of area codes: {}".format(len(set(area_list))))
list_area_codes()
def both_080():
	count = 0
	both = 0
	for item in calls:
		# print(item[0][0:5])
		if (item[0][0:5] or item[1][0:5]=="(080)"):
			count += 1
			if (item[0][0:5] and item[1][0:5]=="(080)"):
				both +=1
	print("percentage both (080): % {:0.2f} ".format(100*both/count))

both_080()
# print(calls)