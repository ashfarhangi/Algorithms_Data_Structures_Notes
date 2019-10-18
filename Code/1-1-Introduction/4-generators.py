def all_odd_for():
	n = 0
	# while True:
	for i in range(10):
		i += 1
		n += 1	
		if (n % 2 != 0):
			print(n)


def all_odd():
	n = 0
	while True:
		n += 1	
		if (n % 2 != 0):
			yield n
my_gen = all_odd()

my_gen.__next__()
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
for i in range(20):
	print(next(my_gen))