#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
  friends = ["Rolf", "Jen", "Anne"]

  for friend in friends:
    print(friend)

  elements = [0,1,2,3,4,5,6,7,8,9]

  # The same as for index in elements: when you don't want to use the index only run the times
  for _ in elements:
    # print(index)
    print("Hello, World!")

  for index in range(10):
    print("Hello, world 2!")

  # Range from 5 to 10
  for index in range(5, 10):
    print("Hello, world 3!")

  # Range from 2 to 20 counting each 3 numbers
  for index in range(2, 20, 3):
    print("Hello, world 4! " + str(index))

  # Dictionaries
  students = [
    {"name": "Rolf", "grade": 90}, 
    {"name": "Bob", "grade": 78}, 
    {"name": "Jen", "grade": 90}, 
    {"name": "Anne","grade": 80}, 
  ]

  for student in students:
    name = student["name"]
    grade = student["grade"]

    print(f"{name} has a grade of {grade}.")

if __name__ == "__main__":
  main()