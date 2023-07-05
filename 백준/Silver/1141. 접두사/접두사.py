n = int(input())
words = sorted(list(set([input() for _ in range(n)])), key=lambda x: len(x))
check = [0] * n
for i in range(len(words)):
    for w in words:
        if len(w) >= len(words[i]):
            if words[i] == w[:len(words[i])]:
                check[i] += 1
print(check.count(1))