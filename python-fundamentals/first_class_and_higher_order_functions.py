#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
  greet()

  # Cloning the function
  hello = greet

  # Calling the clone function
  hello()

  # Calling the before_and_after function and seding the greet function to it without calling
  before_and_after(greet)


def before_and_after(func):
  print("Before...")
  func()
  print("After...")

def greet():
  print("Hello")


operations = {
  "average" : lambda seq: sum(seq) / len(seq),
  "total" : sum, # lambda seq: sum(seq),
  "top" : max , # lambda seq: max(seq)
}

students = [
  {"name":"Rolf", "grades": { 67, 90, 95, 100}},
  {"name":"Bob", "grades": { 56, 78, 80, 90}},
  {"name":"Jen", "grades": { 98, 90, 95, 99}},
  {"name":"Anne", "grades": { 100, 100, 95, 100}}
]

for student in students:
  name = student["name"]
  grades = student["grades"]

  print(f"Student: {name}")
  operation = input("Enter 'average', 'total' or 'top': ")

  result = operations[operation](grades)
  print(result)



if __name__ == "__main__":
  main()