def print_reversed_list_integer(my_list=[]):
    l = len(my_list)
    while l > 0:
        l -= 1
        print("{:d}".format(my_list[l]))
