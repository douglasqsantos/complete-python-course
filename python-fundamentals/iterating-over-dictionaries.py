#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
  friends_ages = {"Rolf": 25, "Anne": 37, "Charlie": 31, "Bob": 22}

  # The keys
  for name in friends_ages:
    print(name)

  # The values of the keys
  for name in friends_ages.values():
    print(name)

  # The key and values
  for name,age in friends_ages.items():
    print(f"{name} is {age} years old.")

if __name__ == "__main__":
  main()