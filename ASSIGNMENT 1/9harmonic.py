#	10 harmonic divisor numbers - harmonic mean of divisors is integer

import statistics
print("Frist 10 harmonic divisor numbers are:\n")

divisors = []  #list to store divisors
count = 0  #to find number of harmonic divisor numbers

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

for i in range (1,9000):
	if count >= 10:
		break
	divisors = [j for j in range(1, i + 1) if i % j == 0]
	harmonic__mean = statistics.harmonic_mean(divisors)
	is_integer_num(harmonic__mean)
	if is_integer_num(harmonic__mean):
		print(i)
		count +=1
