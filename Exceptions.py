def operation(n_list):
    try:
        output = int(n_list[0] / n_list[1])
        print(output)
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError:
        if n_list[0].isdigit():
            print(f"Error Code: invalid literal for int() with base 10: '{n_list[1]}'")
        else:
            print(f"Error Code: invalid literal for int() with base 10: '{n_list[0]}'")

n = int(input())
for _ in range(n):
    string = input().split()
    num_list = []
    try:
        num_list = [int(element) for element in string]
    except ValueError:
        if string[0].isdigit():
            print(f"Error Code: invalid literal for int() with base 10: '{string[1]}'")
        else:    
            print(f"Error Code: invalid literal for int() with base 10: '{string[0]}'")
        continue
    else:
        operation(num_list)
