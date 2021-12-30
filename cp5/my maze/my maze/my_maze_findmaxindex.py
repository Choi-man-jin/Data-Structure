class PriorityQueue:
	def __init__(self):
		self._Items = list()

	def isEmpty(self):
		return len(self._Items) == 0

	def size(self):
		return len(self._Items)

	def enqueue(self, item):
		self._Items.append(item)

	def findMaxIndex(self):
		if self.isEmpty(): return None
		else:
			highest = 0
			for i in range(1, self.size()):
				if self._Items[i][2] > self._Items[highest][2]:
					highest = i
			return highest

	def dequeue(self):
		highest = self.findMaxIndex()
		if highest is not None:
			return self._Items.pop(highest)


	def peek(self):
		highest = self.findMaxIndex()
		if highest is not None:
			return self._Items[highest]

	def __str__(self):
		return str(self._Items)


map = [ ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'], 
	   ['1', '1', '0', '0', '0', '1', '0', '0', '0', 'x'], 
	   ['1', '1', '1', '0', '1', '1', '0', '1', '1', '1'],
	   ['1', '1', '1', '0', '1', '0', '0', '1', '1', '1'],
	   ['e', '0', '0', '0', '1', '1', '0', '0', '0', '1'],
	   ['1', '0', '1', '0', '1', '1', '1', '1', '0', '1'],
	   ['1', '0', '1', '0', '1', '1', '0', '0', '0', '1'],
	   ['0', '0', '1', '0', '1', '1', '0', '1', '0', '1'],
	   ['1', '1', '1', '0', '0', '0', '0', '1', '1', '1'],
	   ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'] ]

MAZE_SIZE = 10

import math
(ox, oy) = (9, 1)
def dist(x, y):
	(dx, dy) = (ox-x, oy-y)
	return math.sqrt(dx*dx + dy*dy)


def isValidPos(x, y):
	if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
		return False
	else:
		return map[y][x] == '0' or map[y][x] == 'x'

def MySmartSearch():
	q = PriorityQueue()
	q.enqueue((0, 4, -dist(0, 4)))
	print('PQueue: ')

	while not q.isEmpty():
		here = q.dequeue()
		print(here[0:2], end = '->')
		x, y, _ = here
		if(map[y][x] == 'x') : return True
		else:
			map[y][x] = '.'
			if isValidPos(x, y-1): q.enqueue((x, y-1, -dist(x, y-1)))
			if isValidPos(x, y+1): q.enqueue((x, y+1, -dist(x, y+1)))
			if isValidPos(x-1, y): q.enqueue((x-1, y, -dist(x-1, y)))
			if isValidPos(x+1, y): q.enqueue((x+1, y, -dist(x+1, y)))
		print('우선순위 큐: ', q)
	return False

result = MySmartSearch()
if result : print(' --> 미로탐색 성공')
else: print(' --> 미로탐색 실패')