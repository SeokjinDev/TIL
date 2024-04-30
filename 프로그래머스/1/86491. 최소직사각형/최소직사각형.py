def solution(sizes):
    mw, mh = 0, 0
    for size in sizes:
        if size[0] < size[1]:
            size.reverse()
        if size[0] > mw:
            mw = size[0]
        if size[1] > mh:
            mh = size[1]

    answer = mw*mh
    return answer