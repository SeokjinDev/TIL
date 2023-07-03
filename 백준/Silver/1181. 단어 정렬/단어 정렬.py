n = int(input())
words = set([input() for _ in range(n)])
words = sorted(words)
words = sorted(words, key=lambda x: len(x))
for w in words:
    print(w)