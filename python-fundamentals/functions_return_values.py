#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Information
# Argument: value you pass in to the function
# Parameter: variable that accepts a value inside the function

def main():
  for car in cars:
    print_car_info(car)

  print(devide(10,2))
  print(devide(6,0))


cars = [ 
  { "make" : "Ford", "model" : "Fiesta", "mileage": 23000, "fuel_consumed": 460},
  { "make" : "Ford", "model" : "Focus", "mileage": 17000, "fuel_consumed": 350},
  { "make" : "Mazda", "model" : "MX-5", "mileage": 49000, "fuel_consumed": 900},
  { "make" : "Mini", "model" : "Cooper", "mileage": 31000, "fuel_consumed": 235},
]

def calculate_mpg(car):
  mpg = car["mileage"] / car["fuel_consumed"]
  return mpg 


def car_name(car):
  name = f"{car['make']} {car['model']}"
  return name


def print_car_info(car):
  name = car_name(car)
  mpg = calculate_mpg(car)

  print(f"{name} does {mpg} miles per gallon.")


def devide(x, y):
  if y == 0:
    return "You tried to divide by zero!"
  else:
    return x / y

if __name__ == "__main__":
  main()