for number in range (100):
    for divisor in range(2, number):
	# If user's number is divisible by the curent divisor, break the loop
	    if number % divisor == 0:
		    print(f"{number} is not prime!")
		    break
    else:
	# This line only runs if no divisors produced integer results
	    print(f"{number} is prime!")