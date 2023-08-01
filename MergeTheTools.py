def merge_the_tools(s, k):
    substrings = [s[i:i+k] for i in range(0, len(s), k)]
    for substring in substrings:
        print(''.join(sorted(set(substring), key=substring.index)))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
