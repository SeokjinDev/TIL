def solve(a, b, c):
    tmp = (b**2 - 4*a*c) ** 0.5
    s1 = (-b + tmp) / (2*a)
    s2 = (-b - tmp) / (2*a)
    return f"{s1:.3f}, {s2:.3f}"

for _ in range(int(input())):
    print(solve(*map(float, input().split())))