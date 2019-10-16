a = [1,2,3,4,0]

def smallest(a):
	key = a[0]
	o = 0
	for i in range(len(a)-1):
		o = o+ 1
		if (a[i]<=key):
			key = a[i]
	print(key,o)

smallest(a)

def biggest(a):
	key = a[0]
	o = 0
	for i in range(len(a)-1):
		o = o+ 1
		if (a[i]>=key):
			key = a[i]
	print(key,o)
biggest(a)

def biggestAndSmallest(a):
	key = a[0]
	o = 0
	for i in range(len(a)-1):
		o = o+ 1
		if (a[i]>=key):
			key = a[i]
	#drop it 
	for i in range(len(a)-1):
		o = o+ 1
		if (a[i]<=key):
			key = a[i]
	print(key,o)

biggestAndSmallest(a)

array1 = [1,2,3,-5,1,0,2]
"""
input: [1,3,5]
output: [1,5]


"""
def smallestAndLargest() 