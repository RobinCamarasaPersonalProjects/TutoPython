def ex_1(character):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return alphabet.index(character) + 1


def ex_2(string):
    result = []
    for i in string:
        result.append(ex_1(i))
    return result


def ex_3(n):
    prime = [True] * (n+1)
    prime[0] = False
    prime[1] = False
    result = []
    for i in range(2, n+1):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
    for i, item in enumerate(prime):
        if item:
            result.append(i)
    return result


