#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():

  for n in range(2, 10):
    for x in range(2, n):
      if n % x == 0:
        print(f"{n} equals {x} * {n//x}")
        break
    else:
      print(f"{n} is a prime number.")

if __name__ == "__main__":
  main()