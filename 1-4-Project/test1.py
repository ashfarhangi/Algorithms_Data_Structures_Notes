arg1 = [1234,12342,13243,1234,51,1234]
print(arg1)
idx = 0
for i in range(10):
	if(arg1.count(1234)!=0):
		idx = arg1.index(1234,idx)
		print(idx)
		del arg1[idx]
		idx +=1
print(arg1)