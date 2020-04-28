#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
  # friend1 = "Ralf"
  # friend2 = "Bob"
  # friend3 = "Anne"

  friends = ["Ralf", "Bob", "Anne"]
  print(friends[0])
  print(friends[1])
  print(len(friends))
  friends.append("Jen")
  print(friends)
  friends.remove("Bob")
  print(friends)

  friends = [["Ralf", 24], ["Bob", 30], ["Anne", 27]]
  print(friends[0][0])
  print(friends[1][1])

  # Just formmating the list
  friends = [
    ["Ralf", 24],
    ["Bob", 30],
    ["Anne", 27]
  ]
  print(friends[0][0])
  print(friends[1][1])


if __name__ == "__main__":
  main()