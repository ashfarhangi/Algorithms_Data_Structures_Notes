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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
def head_tail(text,call):

	"""Summary
	input: list
	output: print message show head and tail
	"""
	arg1 = text[0]
	print("First record of texts,",arg1[0],"texts",arg1[1],"at time",arg1[2])
	arg2 = call.pop()
	print("Last record of calls",arg2[0],"texts",arg2[1],"at time",arg2[2])

head_tail(texts,calls)