#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
  currencies = (0.8, 1.2)
  usd, eur = currencies
  print(usd)
  print(eur)

  friends = [("Rolf", 25), ("Anne", 37), ("Charlie", 31), ("Bob", 22)]
  for name, age in friends:
    print(f"{name} is {age} years old.")

  # Equivalent
  for friend in friends:
    # This
    name, age = friend

    # Or this
    name = friend[0]
    age = friend[1]

if __name__ == "__main__":
  main()