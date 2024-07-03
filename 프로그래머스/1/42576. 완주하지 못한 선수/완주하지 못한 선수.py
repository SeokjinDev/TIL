def solution(participant, completion):
    dic = {}
    hashsum = 0
    
    for i in participant:
        dic[hash(i)] = i
        hashsum += hash(i)
        
    for j in completion:
        hashsum -= hash(j)
    
    return dic[hashsum]