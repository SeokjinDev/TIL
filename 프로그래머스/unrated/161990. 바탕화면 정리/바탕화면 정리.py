def solution(wallpaper):
    yl, xl = len(wallpaper), len(wallpaper[0])
    locs = []
    for i in range(yl):
        for j in range(xl):
            if wallpaper[i][j] == '#':
                locs.append([i, j])
    s1 = sorted(locs)
    s2 = sorted(locs, key=lambda x: x[1])
    answer = [s1[0][0], s2[0][1], s1[-1][0]+1, s2[-1][1]+1]
    return answer