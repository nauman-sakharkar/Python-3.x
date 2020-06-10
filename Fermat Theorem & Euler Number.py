def euler_number(number):
	temp_number = number
	factors = set()
	while temp_number>1:
		for i in range(2,temp_number+1):
			if (temp_number%i==0):
				factors.add(i)
				temp_number = temp_number // i
				break
		
	euler_number = 1
	for factor in factors:
		euler_number = euler_number * (1-(1/factor))
	euler_number = euler_number * number
	return int(euler_number)
print("Euler number of 9 is",euler_number(9))

def fermat_theorem(x,y,m):
	if y == 0:
		return 1
	p = fermat_theorem(x,y//2,m) % m
	p = (p * p) % m
	return (x*p) % m if y%2 else p
a = 3
m = 11
print("Modular inverse of 3 and 11 is",fermat_theorem(a,m-2,m))
