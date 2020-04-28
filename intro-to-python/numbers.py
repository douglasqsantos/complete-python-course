#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():

  # Integers are whole numbers.
  age = 35
  print(age)
  # Floats are numbers with a decimal point
  PI = 3.14159
  print(PI)

  maths_operation = 1 + 3 * 4 / 2 - 2
  print(maths_operation)

  # Division always return float numbers
  float_division = 12 /3 
  print(float_division)

  # Force the division return the integer number
  # This kind of division will not around the number
  integer_division = 13 // 5
  print(integer_division)

  # Modules
  remainder = 13 % 5
  print(remainder)

  # Even numbers always remainder = 0
  # 10 / 2
  # 14 / 2
  # 6 / 2
  # 340 / 2

  # Odd numbers always remainder != 0
  # 11 / 2 
  # 27 / 2
  # 3 / 2

  x = 37
  remainder = x % 2
  print(remainder)





if __name__ == "__main__":
  main()