#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
  
  friends = ["Rolf", "Charlie", "Anna", "Bob", "Jen"]
  print(friends[2:4]) # from 2 until 3 stops at 4
  print(friends[1:]) # Except the first one
  print(friends[:4]) # Except the last one
  print(friends[:]) # Gets a new list of elements
  print(friends[-3:]) # starting from the end
  print(friends[:-2]) # Except the two last ones
if __name__ == "__main__":
  main()