def get_initials(c):
    full_name = c.split(" ")
    i = (len(full_name))
    new_list = []
    for w in range(0, i):  # this loop leaves last name and creates a new list.
        word = full_name[w]
        word = word[0:1].upper()  # sliced word into initial letter
        new_list.append(word) # added last name to the list before joining.
    initial = ''.join(new_list)
    # print("The initial of your name is {0}.".format(initial))
    return initial

print(get_initials(input("Enter your name: ")))

