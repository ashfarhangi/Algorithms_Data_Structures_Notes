target = 18
numOperation = 6

def minOperations(target:int) -> int:
	steps = 0
	while(target!=0):
		while(target/ 2) == (target//2):
			target = target // 2
			steps += 1


		target -=1 
		steps +=1

	return steps

def test_function(test_case):
    target = test_case[0]
    solution = test_case[1]
    output = minOperations(target)
    
    if output == solution:
        print("Pass")
    else:
        print("Fail")
target = 18
solution = 6
test_case = [target, solution]
test_function(test_case)
target = 69
solution = 9
test_case = [target, solution]
test_function(test_case)
