from itertools import combinations

def solution(l):
    l.sort(reverse=True) # decreasing order
    for i in range(len(l), 0, -1):
        for comb in combinations(l, i):
            if sum(comb) % 3 == 0:
                return buildInt(comb)
    return 0

def buildInt(l):
    l = list(l)
    l.reverse()
    res = 0
    size = len(l) - 1
    while size >= 0:
        res *= 10
        res += l[size]
        size -= 1
  
    return res