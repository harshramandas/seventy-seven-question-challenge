A = [int(x) for x in input("Enter elements: ").split(" ")]

for i in range(1,len(A)):
	j = i
	while j > 0:
		if A[j] < A[j-1]:
			A[j], A[j-1] = A[j-1], A[j]
			j -= 1
		else:
			break
for x in A:
	print(x)