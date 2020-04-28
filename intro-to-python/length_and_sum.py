#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
  grades = [80, 75, 90, 100]

  total = sum(grades)
  print(total)

  length = len(grades)
  print(length)

  average = total / length
  print(average)

if __name__ == "__main__":
  main()