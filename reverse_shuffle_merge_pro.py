def frequency(s):
    res = defaultdict(int)
    for char in s:
        res[char] += 1
    return res

# Complete the reverseShuffleMerge function below.
def reverse_shuffle_merge(s):
    char_freq = frequency(s)
    used_chars = defaultdict(int)
    remain_chars = dict(char_freq)
    res = []
    
    def can_use(char):
        return (char_freq[char] // 2 - used_chars[char]) > 0
    
    def can_pop(char):
        needed_chars = char_freq[char] // 2
        return used_chars[char] + remain_chars[char] - 1 >= needed_chars
    
    for char in reversed(s):
        if can_use(char):
            while res and res[-1] > char and can_pop(res[-1]):
                removed_char = res.pop()
                used_chars[removed_char] -= 1
            
            used_chars[char] += 1
            res.append(char)
        
        remain_chars[char] -= 1
    
    return "".join(res)