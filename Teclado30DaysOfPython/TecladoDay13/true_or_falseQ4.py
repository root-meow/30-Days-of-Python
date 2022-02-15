
def prime_finder(dividend):
    divisor = 2

    # Keep looping until the divisor equals the number we're testing
    while divisor < dividend:
        # If user's number is divisible by the curent divisor, break the loop
        if dividend % divisor == 0:
            return "false"
            break

        # Increment the divisor for the next iteration
        divisor = divisor + 1
    else:
        # This line only runs if no divisors produced integer results
        return "True"
print(prime_finder(7))