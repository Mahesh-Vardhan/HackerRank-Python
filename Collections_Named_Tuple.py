N = int(input())
names = input().split()
index_num = names.index("MARKS")
marks = 0

for _ in range(0, N):
    Data_Input = input().split()
    Data_Input[index_num] = int(Data_Input[index_num])
    marks = marks+Data_Input[index_num]
Avg_marks = marks/N
rounded_avg = "{:.2f}".format(Avg_marks)
print(rounded_avg)
