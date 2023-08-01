def print_rangoli(size):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    characters = alphabet[:size]

   
    row_width = 4 * size - 3
    for i in range(size - 1, -size, -1):
        pattern = '-'.join(characters[size - 1:abs(i):-1] + characters[abs(i):size])
        print(pattern.center(row_width, '-'))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
