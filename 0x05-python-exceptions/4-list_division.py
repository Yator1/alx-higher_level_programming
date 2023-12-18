#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    try:
        for i in range(list_length):
            try:
                div1 = my_list_1[i]
                div2 = my_list_2[i]
                if isinstance(div1, (float, int)) and isinstance(div2, (float, int)):
                    try:
                        division = div1 / div2
                        result.append(division)
                    except ZeroDivisionError:
                        print("division by 0")
                        result.append(0)
                else:
                    print("wrong type")
                    result.append(0)
            except IndexError:
                print("out of range")
                result.append(0)
    finally:
        return result
