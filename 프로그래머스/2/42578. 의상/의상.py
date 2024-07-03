from collections import Counter
def solution(clothes):    
    ans = 1
    cs = Counter([c[1] for c in clothes])
    for c in cs:
        ans *= cs[c]+1
    
    return ans-1