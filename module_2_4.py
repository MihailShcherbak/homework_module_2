numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):
    num = int(numbers[i])


    def is_prime(number):
        if number < 2:
            return False
        for k in range(2, int(number ** 0.5) + 1):
            if number % k == 0:
                return False
        return True


    try:
        if num <= 1:
            continue
        elif is_prime(num):
            primes.append(numbers[i])
        else:
            not_primes.append(numbers[i])
    except:
        continue
print('Primes:', primes)
print('Not Primes:', not_primes)
