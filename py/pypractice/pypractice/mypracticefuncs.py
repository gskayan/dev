

def _generate_prime_list(num: int):
    primes = []
    for i in range(1, num+1):
        r = [d for d in range(1, num+1) if i % d == 0]
        if 2 == len(r) and 1 == r[0] and i == r[1]:
            primes.append(i)
    return primes
