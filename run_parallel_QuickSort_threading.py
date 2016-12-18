import threading, random, time
from quicksort import * 
from merge import merge 

class SortingThread (threading.Thread):

	def __init__(self, threadID, name, A, l, h):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.A = A
		self.l = l
		self.h = h
		self.result = list()
	
	def run(self):
		quickSort(self.A, self.l, self.h)
		self.result = self.A[self.l:self.h+1]

class MergingThread (threading.Thread):

	def __init__(self, threadID, name, A, l, h, p):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.A = A
		self.l = l
		self.h = h
		self.p = p
		self.result = list()
	
	def run(self):
		i = self.threadID
		#print("{},{},{},{}".format(l, m, h, p))
		m = self.l + (self.h - self.l)/2
		if self.p == 2:
			t1 = SortingThread(i+1, "SortingThread-{}".format(i+1), self.A, self.l, m)
			t2 = SortingThread(i+2, "SortingThread-{}".format(i+2), self.A, m+1, self.h)
		else:
			t1 = MergingThread(i+1, "MergingThread-{}".format(i+1), self.A, self.l, m, self.p/2)
			t2 = MergingThread(i+2, "MergingThread-{}".format(i+2), self.A, m+1, self.h, self.p/2)

		t1.start()
		t2.start()
		t1.join()
		t2.join()
		self.result = merge(t1.result, t2.result)

if __name__ == '__main__':
	p = 32
	A = list(range(0,1000000))
	random.shuffle(A)

	start_time = time.time()
	t = MergingThread(1, "MergingThread-{}".format(1), A, 0, len(A)-1, p)
	t.start()
	t.join()
	end_time = time.time()
	print(end_time)
	print("{} seconds".format(end_time - start_time))
	#print("{},{}".format(t.result[0], t.result[len(t.result)-1]))

