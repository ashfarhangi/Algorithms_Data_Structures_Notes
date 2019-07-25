# tldr its about using keys and assigning vectors to them
my_dict = {'a':[0, 1, 2, 3], 'b':[0, 1, 2, 3], 'c':[0, 1, 2, 3], 'd':[0, 1, 2, 3]}
i=0
output = []
for key in my_dict:
	output.append(my_dict[key][i])
	i+=1
print(output)
# answer: [0, 1, 2, 3]

print(my_dict['a'])
for key in my_dict:
	print(key)

	"""[0, 1, 2, 3]
[0, 1, 2, 3]
a
b
c
d"""