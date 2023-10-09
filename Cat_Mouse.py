def catAndMouse(x, y, z):
    distance_cat_a = abs(z - x)
    distance_cat_b = abs(z - y)

    if distance_cat_a < distance_cat_b:
        return "Cat A"
    elif distance_cat_b < distance_cat_a:
        return "Cat B"
    else:
        return "Mouse C"
N = int(input())
for _ in range(N):
    pos = [int(n) for n in input().split()]
    Cat_A = pos[0]
    Cat_B = pos[1]
    Mouse_C = pos[2]

    result = catAndMouse(Cat_A, Cat_B, Mouse_C)
    print(result)