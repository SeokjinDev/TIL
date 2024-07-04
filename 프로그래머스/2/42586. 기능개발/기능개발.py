from math import ceil
def solution(progresses, speeds):
    maxNum, answer = 0, []
    for i, j in zip(progresses, speeds):
        end = int(ceil((100-i)/j))
        if maxNum < end:
            answer.append(1)
            maxNum = end
        else:
            answer[-1] += 1
    return answer