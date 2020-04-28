#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
  # short_tuple = "Rolf", "Bob"
  # a_bit_clear = ("Rolf", "Bob")

  # tuple_in_list = [("Rolf", "Bob")]

  friends = ("Rolf", "Bob", "Anne")
  # friends.append("Jen") There is no method append to tuple
  friends = friends + ("Jen",)
  print(friends)

  ## List you can add or remove elements, tuples you can not

if __name__ == "__main__":
  main()