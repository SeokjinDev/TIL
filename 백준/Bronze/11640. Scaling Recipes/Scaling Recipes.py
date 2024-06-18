for i in range(int(input())):
    r, p, d = map(int, input().split())
    scale = d / p
    recipe = []
    for _ in range(r):
        name, weight, per = input().split()
        recipe.append([name, weight:=float(weight), per:=float(per)])
        if per == 100:
            mainW = weight * scale
    print(f"Recipe # {i+1}")
    for j in range(r):
        print(f"{recipe[j][0]} {mainW * (recipe[j][2]/100):.1f}")
    print("-"*40)