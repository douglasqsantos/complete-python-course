#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
  my_name = "Jose"
  your_name = input("Enter your name: ")

  print(f"Hello {your_name}. My name is {my_name}")

  age = input("Enter your age: ")
  age_num = int(age)
  print(f"You have lived for {age_num * 12} months.")

  # Another way to get input as integer
  age = int(input("Enger your age: "))
  months = age * 12
  print(f"You have lived for {months} months.")

if __name__ == "__main__":
  main()