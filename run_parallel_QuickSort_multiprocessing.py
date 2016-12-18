import random, time
from quicksort import * 
from merge import merge 
from multiprocessing import Process, Manager

def multiSorter(A, l, h, p, R):
	R1 = manager.list()
	R2 = manager.list()
	m = l + (h - l)/2
	if p == 2:
		p1 = Process(target=quickSort, args=(A, l, m ))
		p2 = Process(target=quickSort, args=(A, m+1, h))
		p1.start()
		p2.start()
		p1.join()
		p2.join()
		R.extend(merge(A[l:m+1], A[m+1:h+1]))
	else:
		p1 = Process(target=multiSorter, args=(A, l, m, p/2, R1))
		p2 = Process(target=multiSorter, args=(A, m+1, h, p/2, R2))
		p1.start()
		p2.start()
		p1.join()
		p2.join()
		R.extend(merge(R1, R2))

if __name__ == '__main__':
	manager = Manager()
	p = 4
	A = manager.list(range(0,40000))
	random.shuffle(A)

	start_time = time.time()
	R3 = manager.list()
	pz = Process(target=multiSorter, args=(A, 0, len(A)-1, p, R3))
	pz.start()
	pz.join()
	end_time = time.time()
	print("{} seconds".format(end_time - start_time))
	print("{},{}".format(R3[0], R3[len(R3)-1]))


