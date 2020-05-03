#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
  cars = ["ok","ok","ok","faulty","ok","ok"]

  for status in cars:
    if status == "faulty":
      print("Stopping the production line!")
      break
    print(f"This car is {status}")
    print("Shipping new car to customer!")
  # This else will be execute with there is no break and no errors
  else:
    print("All cars built successfully. No faulty cars!")

if __name__ == "__main__":
  main()