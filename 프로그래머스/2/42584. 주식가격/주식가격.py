def solution(prices):
    ans = []
    for i in range(len(prices)):
        time = 0
        for j in range(i+1, len(prices)):
            time += 1
            if prices[i] > prices[j]:
                break
        ans.append(time)
    return ans