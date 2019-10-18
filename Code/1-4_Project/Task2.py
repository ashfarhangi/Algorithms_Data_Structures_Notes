"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
def longest_call_tele_num():
	# print(calls)
	time_spent_list=[]
	for i in range(len(calls)):
		time_spent_list.append(int(calls[i][3]))
	count=0
	i = 0
	for item in time_spent_list:
		i+=1
		if (item > count):
			count = item
			index = i

	print("{} spent the longest time, {} seconds, on the phone during \
		September 2016.".format(calls[index][0],count))
longest_call_tele_num()