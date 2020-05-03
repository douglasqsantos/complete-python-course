#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
  numbers = [0,1,2,3,4]
  doubled_numbers = []

  for number in numbers:
    doubled_numbers.append(number * 2)
    print(doubled_numbers)

  # the same as above
  doubled_numbers = [number * 2 for number in numbers]
  print(doubled_numbers)

  doubled_numbers = [number * 2 for number in range(5)]
  print(doubled_numbers)


  friends_ages = [22,31,35,37]
  age_strings = [f"My friend is {age} years old." for age in friends_ages]
  print(age_strings)

  names = ["Rolf", "Bob", "Jen"]
  lower = [name.lower() for name in names]
  print(lower)
  

  friend = input("Enter your friend name: ")
  friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]
  friends_lower = [name.lower() for name in friends]

  if friend.lower() in friends_lower:
    print(f"{friend.title()} is one of your friends.")


if __name__ == "__main__":
  main()