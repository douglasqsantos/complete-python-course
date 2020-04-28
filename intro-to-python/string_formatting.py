#!/usr/bin/python3
# -*- coding: utf-8 -*-

def main():
  
  age = 34
  age_as_str = str(age)
  print("You are " + age_as_str)

  """
  Information for Python >= 3.6
  However, at the moment f-strings don't work in Udemy's code editor.
  When you're doing our coding exercises, you must use str() instead of f-strings whenever you need
  to add a string
  """
  print(f"You are {age}")

  name = "Douglas"
  greeting = f"How are you, {name}?"
  print(greeting)

  final_greeting = "How are you, {}?"
  jose_greeting = final_greeting.format(name)
  print(jose_greeting)

  bob_greeting = final_greeting.format("Bob")
  print(bob_greeting)

  # Another example
  name = "Jose"
  final_greeting = "How are you, {name}?"
  jose_greeting = final_greeting.format(name="Jose")
  print(jose_greeting)

if __name__ == "__main__":
  main()