A = [int(x) for x in input("Enter elements: ").split(" ")]

# A.sort()

x = int(input("Enter no. to search: "))

def binarySearch(A, x, f, l):
	mid = (f + l)//2
	if l == f:
		if A[mid] == x:
			return mid
		else:
			return -1
	else:
		if A[mid] == x:
			return mid
		elif x < A[mid]:
			return binarySearch(A, x, f, mid - 1)
		else:
			return binarySearch(A, x, mid+1, l)
print(binarySearch(A, x, 0, len(A)-1))