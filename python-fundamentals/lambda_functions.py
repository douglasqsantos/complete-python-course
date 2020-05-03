#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
  pass

# def devide(x,y):
#   return x / y

# The same as above
devide = lambda x, y: x / y

## Calling directly without name
(lambda x, y: x / y)(15, 3)

## Calling directly without name and printing
print((lambda x, y: x / y)(15, 3))

print(devide(15,3))


# def average(sequence):
#   return sum(sequence) / len(sequence)
average = lambda sequence: sum(sequence) / len(sequence)

students = [
  {"name":"Rolf", "grades": { 67, 90, 95, 100}},
  {"name":"Bob", "grades": { 56, 78, 80, 90}},
  {"name":"Jen", "grades": { 98, 90, 95, 99}},
  {"name":"Anne", "grades": { 100, 100, 95, 100}}
]

for student in students:
  print(average(student["grades"]))


if __name__ == "__main__":
  main()