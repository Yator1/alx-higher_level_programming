#!/usr/bin/python3
def search_replace(my_list, search, replace):
    end_list = []
    for i in my_list:
        if i == search:
            end_list.append(replace)
        else:
            end_list.append(i)
    return end_list
