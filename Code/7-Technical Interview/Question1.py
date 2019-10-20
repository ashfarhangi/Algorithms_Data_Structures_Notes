from collections import deque
m =[[1,0,1],[1,0,0]]
def islandFinder(m):
	if(m == [] or m == None):
		return 0
	# Initiate variable count
	numIsland = 0
	#number of elements
	r = len(m)
	# number of rows just check the number of elements inside each element.
	c = len(m[0])
	print("number of rows:",r)
	print("number of columns:",c)
	for i in range(r):
		for j in range(c):
			# if m[i,]
			if (m[i][j] == 1):
				numIsland+=1
				#Now we need breath first search?
				findPartsOfIsland(i,j)
	print(numIsland)
	# need to learn depth search first algorithm for trees.
def findPartsOfIsland(i,j):
	q = deque()
	q.append([i,j])
	while(len(q!=0)):
		x = q.pop()
		y = i[1]
# Talk about the purpose of your code
# use a que to get 
# First thing i want do to is initiatlize
# since we are using. First
islandFinder(m)