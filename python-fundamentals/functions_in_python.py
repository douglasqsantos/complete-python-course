#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
  greet()


def greet():
  name = input("Enter your name: ")
  print(f"Hello, {name}!")

if __name__ == "__main__":
  main()