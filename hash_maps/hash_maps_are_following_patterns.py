def solution(strings, patterns):
    str_map = {}
    pat_map = {}
    for i in range(len(strings)):
        str_map[strings[i]] = str_map.get(strings[i],patterns[i])
        pat_map[patterns[i]] = pat_map.get(patterns[i],strings[i])
        if str_map[strings[i]] != patterns[i]: return False
        if pat_map[patterns[i]] != strings[i]: return False
    return True