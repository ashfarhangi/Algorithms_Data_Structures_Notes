def platform_count(arrival:int,departure:int) -> int:
	numPlatform = 0
	
	for time in range(min(arrival),max(departure)+10,10):
		tempNumPlatform=0
		for j in range(len(arrival)):
			if (time>=arrival[j]) and (time<departure[j]):
				tempNumPlatform += 1
		if (tempNumPlatform > numPlatform):
			numPlatform=tempNumPlatform
	print(numPlatform)	
	return numPlatform
def test_function(test_case):
	arrival = test_case[0]
	departure = test_case[1]
	answer = test_case[2]
	output = platform_count(arrival,departure)
	if output == answer:
		print(True)
	else:
		print(False)

	# for i in range(len(arrival)):
		# platform_count(arrival[i],departure[i])

arrival = [900,  940, 950,  1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
test_case = [arrival, departure, 3]

test_function(test_case)

arrival = [200, 210, 300, 320, 350, 500]
departure = [230, 340, 320, 430, 400, 520]
test_case = [arrival, departure, 2]
test_function(test_case)


