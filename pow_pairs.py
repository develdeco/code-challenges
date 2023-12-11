# Found in code signal
def isPowTwo(num,memo):
    if num == 0: return False
    if num == 1: return True
    memo[num] = memo.get(num,num%2==0 and isPowTwo(num//2,memo))
    return memo[num]

def solution(a):
    num_map, num_acc, pow_memo = {}, [], {}
    for i,num in enumerate(a):
        num_acc.append(a[i])
        num_map[i] = [*num_acc]
    pairs = 0
    for ix in num_map.keys():
        for num in num_map[ix]:
            if isPowTwo(a[ix]+num,pow_memo):
                pairs += 1
    return pairs