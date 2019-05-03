

def _generate_prime_list(num: int):
    primes = []
    for i in range(1, num+1):
        r = [d for d in range(1, num+1) if i % d == 0]
        if 2 == len(r) and 1 == r[0] and i == r[1]:
            primes.append(i)
    return primes



def str2rangeArgs(s: str, delim: str):
    params = s
    try:
        intlist = [int(i) for i in s.split(delim) if len(i.strip()) > 0]
    except ValueError as ve:
        raise ValueError(f"Input format invalid: '{params}'")

    if len(intlist) < 2:
        raise Exception(f"Insufficient params for range: '{params}'")

    if 2 == len(intlist):
        return [*range(intlist[0], intlist[1])]
    elif 3 >= len(intlist):
        return [*range(intlist[0], intlist[1], intlist[2])]
    else:
        raise Exception(f"Range generation failed: '{params}'")
