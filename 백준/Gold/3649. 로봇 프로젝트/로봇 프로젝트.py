while 1:
    try:
        x = int(input()) * 10000000 # nm to cm
        n = int(input())
        li = sorted([int(input()) for _ in range(n)])
        ans = []
        l, r = 0, n-1
        while l < r:
            if li[l]+li[r] == x:
                ans = [li[l], li[r]]
                break
            if li[l]+li[r] < x:
                l = l+1
            else:
                r = r-1
        if ans:
            print("yes", ans[0], ans[1])
        else:
            print("danger")
    except:
        break