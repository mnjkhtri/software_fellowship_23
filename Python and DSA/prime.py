# Prime Numbers : Number which can be divided by itself or only 1 i.e prime numbers have only two divisors

def n_prime_numbers(n):
    # let's store the primes in list
    primes = []

    # Prime numbers are always greater than 1
    for i in range(2,n):
        # We assume current number is Prime
        is_prime = True

        # We divide the current number by numbers in range(>1, < curr_number).Why?
        for j in range(2,i):
            # if we find any number that can divide the curr. number then the current number is not prime i.e our assumption was false.
            if i % j == 0:
                # so we change the is_prime to False and break out of the loop.
                is_prime = False
                break

        # if is_prime holds True, we append it to the primes list.
        if is_prime:
            primes.append(i)

    
    return primes


# By default, input return is of string type. So we need to change the type.
n = int(input("Enter the number: "))
print(n_prime_numbers(n))
