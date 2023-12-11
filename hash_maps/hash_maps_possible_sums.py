def combinations(elements):
    if len(elements) == 0: return [[{},0]]
    firstEl = elements[0]
    rest = elements[1:]
    
    combsWithoutFirst = combinations(rest)
    combsWithFirst = []
    
    for comb in combsWithoutFirst:
        combWithFirst = [comb[0].copy(),comb[1]]
        combWithFirst[0][firstEl] = combWithFirst[0].get(firstEl,0)+1
        combWithFirst[1] += firstEl
        combsWithFirst.append(combWithFirst)
        
    return [*combsWithoutFirst,*combsWithFirst]

def solution(coins, quantity):
    coin_map = {}
    for i in range(len(coins)):
      coin_map[coins[i]] = coin_map.get(coins[i],0)+quantity[i]

    coins = []
    quantity = []
    for coin in coin_map.keys():
      coins.append(coin)
      quantity.append(coin_map[coin])

    comb_list = combinations(coins)[1:]
    sum_set = set()
    sum_count = 0
    for comb in comb_list:
        if comb[1] not in sum_set:
            sum_set.add(comb[1])
            sum_count += 1

    level = 1
    while len(comb_list) > 0:
        new_comb_list = []
        for i in range(len(coins)):
            quantity[i] -= 1
            if quantity[i] > 0:
                new_coin_combs = []
                for comb in comb_list:
                    if coins[i] in comb[0] and comb[0][coins[i]] == level:
                        new_comb = [comb[0].copy(),comb[1]]
                        new_comb[0][coins[i]] += 1
                        new_comb[1] += coins[i]
                        new_coin_combs.append(new_comb)
                        if new_comb[1] not in sum_set:
                            sum_set.add(new_comb[1])
                            sum_count += 1
                comb_list.extend(new_coin_combs)
                new_comb_list.extend(new_coin_combs)
        comb_list = new_comb_list
        level += 1

    return sum_count

#print(solution([10, 50, 100],[1, 2, 1]))
#print(solution([1, 1, 1, 1, 1],[9, 19, 18, 12, 19]))
#print(solution([3, 1, 1],[111, 84, 104]))
print(solution([1, 2, 3],[2, 3, 10000]))
