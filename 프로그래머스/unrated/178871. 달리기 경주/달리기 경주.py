def solution(players, callings):
    orderPlayer = {}
    orderRank = {}
    for i, p in enumerate(players):
        orderPlayer[p] = i
        orderRank[i] = p

    for c in callings:
        pRank = orderPlayer[c]
        prePlayer = orderRank[pRank-1]

        orderPlayer[c] -= 1
        orderPlayer[prePlayer] += 1
        orderRank[pRank] = prePlayer
        orderRank[pRank-1] = c

    answer = [*orderRank.values()]
    return answer