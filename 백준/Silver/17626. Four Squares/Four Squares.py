def solve(n):
    i = 0
    while i**2 <= n:
        j = i
        while j**2 <= n:
            k = j
            while k**2 <= n:
                l = k
                while l**2 <= n:
                    if i**2 + j**2 + k**2 + l**2 == n:
                        return 4 - [i, j, k, l].count(0)
                    l += 1
                k += 1
            j += 1
        i += 1

n = int(input())
s = solve(n)
print(s)