def quickSort(A,l,r):
	if l < r:
		pivot = A[l]
		s = l
		for i in range(l+1, r):
			if A[i] < pivot:
				s = s + 1
				# Swap Array elements
				A[s], A[i] = A[i], A[s]
		
		A[l], A[s] = A[s], A[l]
		quickSort(A, l, s - 1)
		quickSort(A, s + 1, r)
