#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
  age = int(input("enter your age: "))
  can_learn_programming = age > 0 and age < 150

  print(f"You can learn programming: {can_learn_programming}.")

  usually_working = age >= 18 or age <= 65
  print(f"At {age}, you are usually working: {usually_working}")


  """
  Information

  and gives you the first value if it is False, otherwise it gives you the second value.

  or gives you the first value if it is True, otherwise it gives you the second value.
  """

  # Testing boolean
  print(bool(35)) # True
  print(bool("Raph")) # True
  print("********")
  print(bool(0)) # False
  print(bool("")) # False

  x = 35 and 0 
  print(x)

  x = 0 or 35
  print(x)

  name = ""
  surname = "Smith"
  greeting = name or f"Mr. {surname}"
  print(greeting)

  name = input("Enter your name: ")
  surname = input("Enter your surname: ")
  greeting = name or f"Mr. {surname}"
  print(greeting)

  print(not False)
  print(not True)

if __name__ == "__main__":
  main()