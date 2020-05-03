#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
  
  is_learning = True

  while is_learning:
    print("You're learning!")
    user_input = input("Are you still learning? ")
    is_learning = user_input == "yes"

  print("We stopped running.")

if __name__ == "__main__":
  main()