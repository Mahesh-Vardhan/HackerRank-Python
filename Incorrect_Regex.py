import re
def is_reg(exp):
    try:
        re.compile(exp)
        return True
    except re.error:
        return False
        
n = int(input())
for _ in range(n):
    exp = input()
    print(is_reg(exp))
