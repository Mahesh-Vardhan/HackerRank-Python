numbers = int(input())
money = 0 
sizes_string = input()
size_list = sizes_string.split() 
final_list = [] 
for size in size_list:
    final_list.append(int(size)) 

no_of_input = int(input())
for _ in range(no_of_input): 
    size_string = input()
    inp_string = size_string.split() 
    size_list = []
    for sizes in inp_string:
        size_list.append(int(sizes)) 
    if size_list[0] in final_list:
        money += size_list[1]
        final_list.remove(size_list[0])

print(money)
