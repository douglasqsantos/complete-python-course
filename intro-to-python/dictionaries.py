#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
  
  friends_ages = { "Rolf" : 24, "Adam" : 30, "Anne": 27 }

  print(friends_ages["Rolf"])

  friends_ages["Bob"] = 20
  print(friends_ages)

  friends_ages["Rolf"] = 25
  print(friends_ages)

  friends = (
    { "name": "Rolf Smith", "age" : 24 }, 
    { "name": "Adam Wool", "age" : 30 }, 
    { "name": "Anne Pun", "age" : 27 }
  )

  print(friends[0]["name"])
  print(friends[1]["name"])
  print(friends[2]["name"])

  friend = friends[0]
  print(friend["name"])

  friends = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]
  print(friends)

  friend_age_dic = dict(friends)
  print(friend_age_dic)

if __name__ == "__main__":
  main()