def solution(genres, plays):
    sD, gD, m = {}, {}, []
    answer = []
    for i, g, p in zip(range(len(genres)), genres, plays):
        if sD.get(g): sD[g] += p
        else: sD[g] = p
        m.append([i, g, p])
    
    m = sorted(m, key=lambda x: x[0], reverse=True)
    m = sorted(m, key=lambda x: x[2])
    m = sorted(m, key=lambda x: sD[x[1]])
    while m:
        x = m.pop()
        if gD.get(x[1]):
            if gD[x[1]] < 2:
                gD[x[1]] += 1
            else:
                continue
        else:
            gD[x[1]] = 1
        answer.append(x[0])
    
    
    return answer