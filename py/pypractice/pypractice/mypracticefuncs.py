

def generate_prime_list(num: int):
    primes = []
    for i in range(1, num+1):
        r = [d for d in range(1, num+1) if i % d == 0]
        if 2 == len(r) and 1 == r[0] and i == r[1]:
            primes.append(i)
    return primes


class InvalidInputError(ValueError):
    pass

def str2range(s: str, delim: str):
    params = s
    try:
        def validateInput(s: str):
            import re
            pattern = "\x20*[1-9]+[0-9]?\x20*,\x20*[1-9]+[0-9]?\x20*[,]?\x20*([1-9]+[0-9]?)?\x20*"
            if re.match(pattern, s) is not None:
                return True
            else:
                return False

        if not validateInput(s):
            raise InvalidInputError(f"Invaid input string '{s}'")

        intlist = [int(i) for i in s.split(delim) if len(i.strip()) > 0]

    except InvalidInputError as iie:
        raise iie

    if 2 == len(intlist):
        return [*range(intlist[0], intlist[1])]
    elif 3 >= len(intlist):
        return [*range(intlist[0], intlist[1], intlist[2])]
