#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_val = float('-inf')
    for value in a_dictionary.values():
        if value > max_val:
            max_val = value
    return max_val
