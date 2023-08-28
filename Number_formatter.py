n = int(input())
Input_List = [int(num) for num in input().split()]
positive = 0
negative = 0
neutral = 0
for i in range(n):
    if Input_List[i] > 0:
        positive += 1
    elif Input_List[i] < 0:
        negative += 1
    else:
        neutral += 1        
print("{:.6f}".format(positive/n))
print("{:.6f}".format(negative/n))
print("{:.6f}".format(positive/n))
