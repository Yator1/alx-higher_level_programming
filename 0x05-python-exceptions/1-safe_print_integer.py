#!/usr/bin/python3
def safe_print_integer(value):
  """
  Prints an integer using "{:d}".format() and checks if it was successful.

  Args:
      value: The value to print.

  Returns:
      True if the value was successfully printed as an integer, False otherwise.
  """
  try:
    print("{:d}".format(value))
    return True
  except (ValueError, TypeError):
    return False
