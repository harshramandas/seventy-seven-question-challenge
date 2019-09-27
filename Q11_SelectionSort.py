A = [int(x) for x in input("Enter elements:").split(" ")]

for i in range(len(A)):
	m = A[i]
	mi = i
	for j in range(i,len(A)):
		if A[j] < m:
			m = A[j]
			mi = j
	A[i], A[mi] = A[mi], A[i]
for x in A:
	print(x)