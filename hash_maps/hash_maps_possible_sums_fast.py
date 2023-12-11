def solution(coins, quantity):
    possible_sums = {0}
    for c, q in zip(coins, quantity):
        possible_sums = {x + c * i for x in possible_sums for i in range(q + 1)}
    
    return len(possible_sums) - 1