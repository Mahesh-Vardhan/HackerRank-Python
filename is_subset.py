n  = int(input())
for _ in range(n):
    n1 = int(input())
    set1 = [int(el) for el in input().split()]
    n2 = int(input())
    set2 = [int(el) for el in input().split()]
    set1 = set(set1)
    set2 = set(set2)
    is_subset = set1.issubset(set2)
    if is_subset:
        print("True")
    else:
        print("False")    
