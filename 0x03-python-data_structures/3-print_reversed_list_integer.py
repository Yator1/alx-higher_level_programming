def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    while length > 0:
        length -= 1
        print("{:d}".format(my_list[length]))
