def solution(crypt, solution):
    mapping = {}
    for m in solution:
        mapping[m[0]] = m[1]
    for word in crypt:
        if len(word) > 1 and mapping[word[0]] == '0':
            return False
    a = int(''.join(map(lambda l:mapping[l], crypt[0])))
    b = int(''.join(map(lambda l:mapping[l], crypt[1])))
    c = int(''.join(map(lambda l:mapping[l], crypt[2])))
    return a + b == c