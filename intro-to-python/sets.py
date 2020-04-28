#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Set cannot have duplicates

def main():
  art_friends = { "Rolf", "Anne", "Jen" }
  science_friends = { "Jen", "Charlie" }

  art_but_not_sience = art_friends.difference(science_friends)
  print(art_but_not_sience)

  # difference between them.
  science_but_not_art = science_friends.difference(art_friends)
  print(science_but_not_art)

  # Symmetric difference compare what is not in both
  not_in_both = art_friends.symmetric_difference(science_friends)
  print(not_in_both)

  # intersection check which one is in both
  art_and_science = art_friends.intersection(science_friends)
  print(art_and_science)

  # Union both sets with no duplicates
  all_friends = art_friends.union(science_friends)
  print(all_friends)

  # Appending
  art_friends.add("Jen")
  print(art_friends)

  # Removing
  art_friends.remove("Jen")
  print(art_friends)

  


if __name__ == "__main__":
  main()