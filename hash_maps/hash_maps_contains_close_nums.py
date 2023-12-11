def solution(nums, k):
    num_map = {}
    for ix,num in enumerate(nums):
        num_map[num] = num_map.get(num,ix)
        if ix-num_map[num] > 0:
            if ix-num_map[num] <= k: return True
            else: num_map[num] = ix
    return False