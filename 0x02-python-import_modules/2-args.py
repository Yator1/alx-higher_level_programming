#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    arg_length = len(argv)
    if arg_length == 2:
        print("1 argument:")
    elif arg_length == 1:
        print("0 arguments.")
    else:
        print("{} arguments:".format(arg_length - 1))
    j = 1
    while arg_length > 1:
        print("{}: {}".format(j, argv[j]))
        j += 1
        arg_length -= 1
