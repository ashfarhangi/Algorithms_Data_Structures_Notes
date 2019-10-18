array1 = [1,2,3,-5,1,0,2]
array2 = []
"""
input: [1,3,5]; [] ;None
output: [1,5], None


"""
def smallestAndLargest(arr):
	if(arr == None or arr == []):
		return None

	largest = arr[0]
	smallest = arr[0]
	key = None

	for i in range(len(arr)):
		if(arr[i] <= smallest):
			smallest = arr[i]
		if(arr[i] >= largest):
			largest = arr[i]
	print([smallest,largest])

smallestAndLargest(array1)