#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
  print(add(5,10))
  print(add(5))
  print(add(5,6))
  print(add(x=5, y=2))
  # print(add(x=5, 2)) # Error we need to use the both with name if you use the first one as named argument
  print(add(5,y=2))

  print(1,2,3,4,5, sep=" - ")


def add(x, y=3):
  total = x + y
  return total

if __name__ == "__main__":
  main()