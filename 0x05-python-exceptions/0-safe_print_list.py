#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
  """
  Prints x elements of a list, handling potential errors.

  Args:
      my_list: The list to print from.
      x: The number of elements to print (can be larger than the list length).

  Returns:
      The actual number of elements printed.
  """
  printed_count = 0
  try:
    for i in range(x):
      # Ignore potential index errors if x is larger than the list length
      try:
        print(my_list[i], end="")
        printed_count += 1
      except IndexError:
        pass
    print()  # Print a newline after all elements printed
  except Exception as e:  # Catch any other unexpected errors
    print(f"Error: {e}")
  return printed_count
