#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This is like a multiline comment in C
We can use this to add a bunch of stuff here.
"""

def main():
  my_string = "Hello, World!"
  print(my_string)

  string_with_quotes = "Hello, it's me."
  another_with_quotes = 'Here said "You are amazing!" yesterday.'
  another_with_quotes_backslash = "Here said \"You are amazing!\" yesterday."
  multiline = """Hello, World,

  My name is Douglas. Welcome to my program.
  """

  name = "Douglas"
  greeting = "Hello, " + name
  

  print(string_with_quotes)
  print(another_with_quotes)
  print(another_with_quotes_backslash)
  print(multiline)
  print(greeting)

if __name__ == "__main__":
  main()