string = input()
big_arr = []
fin_arr = []
for letter in string:
    big_arr.append(letter)
for letter in big_arr:
    if letter == letter.upper():
        sm_string = []
        ind = big_arr.index(letter)
        sm_string = big_arr[:ind]
        fin_arr.append(sm_string)
print(len(fin_arr)+1)        
