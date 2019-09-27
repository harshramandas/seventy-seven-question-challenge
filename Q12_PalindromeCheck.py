A = input("Enter to check Palindrome: ")
f = 1
for i in range(0, len(A)//2):
	if A[i] != A[len(A) - i - 1]:
		f = 0
		break
if f == 1:
	print("Palindrome!")
else:
	print("Not Palindrome!")