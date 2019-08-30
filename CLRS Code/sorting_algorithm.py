"""Summary
 use a key to hold the number and keep it in its place if its higher than left ones /or replace it with left ones if its lower
 [5,2] > [2,5]
Attributes:
    A (list): Just a list
"""
A = [5,2,4,6,1,3]

def insertion_sort():
	"""insertaion sort effective 1s
	"""
	for j in range(1,len(A)):
		key = A[j]
		i = j - 1
		while(i>=0 and A[i]>key):
			A[i+1] = A[i]
			i = i-1
		A[i+1] = key
	print(A)

def python_sort():
	"""Tim sort:
	"""
	A.sort()
	print(A)


insertion_sort()
# 0.2s
python_sort()
# 0.1s
