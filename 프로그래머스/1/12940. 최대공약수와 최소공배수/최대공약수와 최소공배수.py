def solution(n, m):
    return gcd(n, m), lcm(n, m)

def gcd(a, b):
    a, b = max(a, b), min(a, b)
    if a % b == 0:
        return b
    else:
        return gcd(b, a%b)
    
def lcm(a, b):
    a, b = max(a, b), min(a, b)
    return a*b // gcd(a, b)