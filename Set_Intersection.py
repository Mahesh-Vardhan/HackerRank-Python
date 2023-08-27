n = int(input())
n_l = input().split()
n_list = [int(num) for num in n_l]
N = int(input())
N_l = input().split()
N_list = [int(num) for num in N_l]
finList = set(n_list).intersection(set(N_list))
print(len(finList))
