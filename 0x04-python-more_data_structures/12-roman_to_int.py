#!/usr/bin/python3
def roman_to_int(roman_string):
  roman_numeral_map = {
      "I": 1,
      "V": 5,
      "X": 10,
      "L": 50,
      "C": 100,
      "D": 500,
      "M": 1000,
  }

  if not roman_string or not isinstance(roman_string, str):
      return 0

  integer_value = 0
  previous_value = 0
  for char in roman_string[::-1]:
      current_value = roman_numeral_map[char]
      if current_value < previous_value:
          integer_value -= current_value
      else:
          integer_value += current_value
      previous_value = current_value
  return integer_value
