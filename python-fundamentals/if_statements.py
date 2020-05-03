#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
  friend = "Rolf"

  user_name = input("Enter your name: ")

  if user_name == friend:
    print("Hello, friend!")
  else:
    print("Hello, stranger!")


  friends = ["Rolf", "Bob", "Anne"]
  family = ["Jen", "Charlie"]

  user_name = input("Enter your name: ")

  ## Check the item into the list
  if user_name in friends:
    print("Hello, friend!")
  elif user_name in family:
    print("Hello, family!")
  else:
    print("I dont't know you")


if __name__ == "__main__":
  main()