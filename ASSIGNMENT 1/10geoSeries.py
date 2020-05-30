#import math
def printgp(a, r, i):
	x = pow(r, i)
	print(a * x)
a = 1
r = int(input("Enter the common ratio of Geometric series\n"))
print("The first 10 terms of the series are")
for i in range(0, 10):
	printgp(a, r, i)
