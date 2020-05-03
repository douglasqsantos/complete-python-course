#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
  ages = [ 22, 35, 27, 21, 20]

  odds = [age for age in ages if age % 2 == 1]

  print(odds)

  friends = ["Rolf","ruth","charlie","Jen"]
  guests = ["jose","Bob","Rolf","Charlie", "michael"]

  friends_lower = set([f.lower() for f in friends])
  guests_lower = set([g.lower() for g in guests])

  print(friends_lower.intersection(guests_lower))

  # without sets
  friends = ["Rolf","ruth","charlie","Jen"]
  guests = ["jose","Bob","Rolf","Charlie", "michael"]

  friends_lower = [f.lower() for f in friends]
  guests_lower = [g.lower() for g in guests]


  present_friends = [
    name.title() for name in guests if name.lower() in friends_lower
  ]

  print(present_friends)

if __name__ == "__main__":
  main()