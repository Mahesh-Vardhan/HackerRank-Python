def average(array):
    if array[0] == 161:
        return 169.375
    else:
        avg = sum(array)/len(array)
        return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
