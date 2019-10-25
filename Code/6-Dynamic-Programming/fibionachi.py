# fibionachi
# input: 1 2 3 4 5 6 7 8 9 10
# output: 1 1 2 3 5 8 13 21 34 55
n = 3
def fib(n):
	if n < 0:
		return False
	elif n== 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1)+fib(n-2)
	print(n)
# o(n^2)
print(fib(10))
#code taken from geeksforgeeks.org
def dynamicFib(n):
	arr = [0,1]
	while (len(arr) < n+1):
		arr.append(0)

	if n < 0:
		return n
	if n<=1:
		return n
	else:
		if arr[n-1] ==0:
			arr[n-1] = dynamicFib(n-1)
		if arr[n-2] == 0:
			arr[n-2] == dynamicFib(n-2)
	arr[n] = arr[n-2] + arr[n-1]
	return arr[n]
print(dynamicFib(2))