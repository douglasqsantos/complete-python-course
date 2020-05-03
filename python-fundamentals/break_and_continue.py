#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
  cars = ["ok","ok","ok","faulty","ok","ok"]

  for status in cars:
    if status == "faulty":
      # print("Stopping the production line!")
      # break
      print("Found faulty car, skipping...")
      continue
    print(f"This car is {status}")
    print("Shipping new car to customer!")

if __name__ == "__main__":
  main()