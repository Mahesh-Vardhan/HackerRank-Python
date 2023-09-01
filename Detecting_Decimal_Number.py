n = int(input())
for _ in range(n):
    Input = input()
    try:
        float(Input)
    except ValueError:
        print(False)    
    else:
        print(True)    
