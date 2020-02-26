#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  recipe = [recipe[x] for x in recipe]
  ingredients = [ingredients[x] for x in ingredients]
  
  if len(ingredients) != len(recipe):
    return 0

  difference = []

  for i in range(0, len(ingredients)):
    difference.append(ingredients[i] - recipe[i])

  smallest_difference = difference[0]
  smallest_index = 0
  for i in range(0, len(difference)):
    if smallest_difference > difference[i]:
      smallest_difference = difference[i]
      smallest_index = i 

  if smallest_difference < 0:
    return 0
  elif smallest_difference == 0:
    return 1
  else: 
    return ingredients[smallest_index] // recipe[smallest_index]


# print((recipe_batches({ 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 })))
# print(recipe_batches({ 'milk': 100, 'butter': 50, 'cheese': 10 }, { 'milk': 198, 'butter': 52, 'cheese': 10 }))



if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))