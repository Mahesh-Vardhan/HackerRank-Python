def Next_Mulitple(number):
    remainder = number % 5
    if remainder == 0:
        return number
    else:
        number += (5 - remainder)
        return number
n = int(input())
for _ in range(n):
    Mark = int(input())
    next_Number = Next_Mulitple(Mark)   
    if (next_Number - Mark) < 3 and Mark >= 38:
        print(next_Number)
    else:
        print(Mark)   
