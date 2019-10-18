bills = [1,2,5,10,20,50,100]
amount = 0

"""
CITBRCD
input = [1,4,2] or [] or None
3.5 
output = integer 
365=3x100 + 1x50 + 1x10 +1 x5 = 6
initiate billCount variable, 
"""
"""Greedy algorithm choosing the best action at each step."""

def countBill(amount,bills):
	if (amount ==0 or amount == None):
		return False
	billCount = 0
	for i in range(1,len(bills)):
		arg1 = amount / bills[-i]
		if ( arg1>= 1):
			arg1 = int(arg1)
			billCount += arg1
			amount = amount - (arg1*bills[-i]) 
	print( billCount)
countBill(amount,bills)

"""
Its not optimal for {1,4,5,10}
for target = 8
5 1 1 1 
rather than 4+4 
"""

