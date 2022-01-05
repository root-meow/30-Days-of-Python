# Get a number to test from the user
dividend = int(input("Please enter a number: "))

# Grab numbers one at a time from the range sequence
for divisor in range(2, dividend):
	# If user's number is divisible by the curent divisor, break the loop
	if dividend % divisor == 0:
		print(f"{dividend} is not prime!")
		break
else:
	# This line only runs if no divisors produced integer results
	print(f"{dividend} is prime!")