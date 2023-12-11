def solution(s, debts, interests):
    sortix = [i[0] for i in sorted(enumerate(interests), key=lambda x:x[1], reverse=True)]
    budget = s*0.1
    total = 0
    while debts[sortix[-1]] > 0:
        mbudget = budget
        for ix in sortix:
            if debts[ix] >= mbudget:
                debts[ix] -= mbudget
                debts[ix] += debts[ix] * (interests[ix] / 100)
                mbudget = 0
            else:
                mbudget -= debts[ix]
                debts[ix] = 0
        total += budget - mbudget
    return total