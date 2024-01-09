#!/usr/bin/python3
def read_file(filename=""):
   """
   Reads a text file (UTF8) and prints its contents to stdout.

   Args:
       filename (str, optional): The name of the file to read. Defaults to "".
       """

   with open(filename,  encoding="utf-8") as f:
           f_contents = f.read()
           print(f_contents)
