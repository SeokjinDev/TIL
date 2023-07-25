def solution(name, yearning, photo):
    d = {}
    for n, y in zip(name, yearning):
        d[n] = y
    
    answer = []
    for ph in photo:
        c = 0
        for p in ph:
            if d.get(p) is not None:
                c += d[p]
        answer.append(c)

    return answer