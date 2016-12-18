import random, time
from quicksort import quickSort

A = list(range(0,1000000))
random.shuffle(A)

start_time = time.time()

quickSort(A, 0, len(A)-1)

end_time = time.time()
print("{} seconds".format(end_time - start_time))

