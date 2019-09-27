A = [int(x) for x in input("Enter elements:").split(" ")]

for i in range(len(A)-1):
	for j in range(len(A) - i - 1):
		if A[j] > A[j+1]:
			A[j], A[j+1] = A[j+1], A[j]

for x in A:
	print(x)