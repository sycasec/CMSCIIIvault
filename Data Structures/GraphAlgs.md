[[DataStructRoot]]

# A Star Search
- Visit each neighbor
- for each neighbor, add to DEQUE, update local score and global score
	-  newLocalScore = current node local score + distance from parent
	- if current local score == -1 or newLocalScore < currentLocalScore
		- update local score
		- update parent
		- newGlobalScore = currentLocalScore + distanceToEnd
		- update global score
	- remove from DEQUE
- after visiting all neighbors, sort DEQUE by lowest → highest
- set DEQUE(0) as CurrentNode
	- visitEachNeighbor()

## End
- trace parent node from end node
- each parent node will have the lowest distance



