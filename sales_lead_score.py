import functools

def solution(names, time, netValue, isOnVacation):
    def compare(x, y):
        score_diff = netValue[y]*time[y]/365 - netValue[x]*time[x]/365
        if score_diff != 0: return score_diff
        else:
            time_diff = time[y] - time[x]
            if time_diff != 0: return time_diff
            else:
                if names[x] < names[y]: return -1
                elif names[x] > names[y]: return 1
                else: return 0
        
    sol = [i[0] for i in filter(lambda x:not x[1], enumerate(isOnVacation))]
    sol = sorted(sol, key=functools.cmp_to_key(compare))
    return list(map(lambda i:names[i], sol))