#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv)
    i = 1
    sum_total = 0
    while args > 1:
        sum_total += int(argv[i])
        i += 1
        args -= 1
    print(sum_total)
