def solution(friends, gifts):
    friendsNum = len(friends)
    numTable = {i:j for i, j in zip(friends, range(friendsNum))}
    logTable = [[0] * friendsNum for _ in range(friendsNum)]

    for giftLog in gifts:
        giftLog: str
        a, b = [numTable[g] for g in giftLog.split()]
        logTable[a][b] += 1
        logTable[b][a] -= 1

    answer = 0

    for i in range(friendsNum):
        cnt = 0
        for j in range(friendsNum):
            if i == j:
                continue
            if logTable[i][j] > 0 or (logTable[i][j] == 0 and sum(logTable[i]) > sum(logTable[j])):
                cnt += 1
        if answer < cnt:
            answer = cnt

    return answer