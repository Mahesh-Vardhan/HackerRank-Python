def mutate_string(string, position, character):
    # Check if the position is within the valid range of the string
    if position < 1 or position > len(string):
        return "Invalid position."

    # Construct the new string by replacing the character at the specified position
    new_string = string[:position - 1] + character + string[position:]

    return new_string

if __name__ == '__main__':
    s = input("Enter the string: ")
    i, c = input("Enter position and character: ").split()

    s_new = mutate_string(s, int(i), c)
    print(s_new)

