def prod(x,y):
	return x*y
def factorial(num):
	n=1
	answer = 1
	while True:
		if (n < num):
			n += 1
			answer = prod(answer,n)
		else:
			yield answer





n=5
print(next(factorial(n)))
print(next(factorial(n)))
print(next(factorial(n)))

# answer
def prod(a,b):
    # TODO change output to the product of a and b
    output = a*b
    return output

def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        i+=1
        n = output
        yield output
        # TODO: update i and n
        # Hint: i is a successive integer and n is the previous product


# Test block
my_gen = fact_gen()
num = 5
for i in range(num):
    print(next(my_gen))

# Correct result when num = 5:
# 1
# 2
# 6
# 24
# 120


