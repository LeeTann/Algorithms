#!/usr/bin/python

# ingredients divide by recipe = total pies
# if any ingredients is missing return 0

import math

def recipe_batches(recipe, ingredients):
  total = None

  # Loop thru the array recipe
  for i in recipe:
    print(i)

    # Chech to see if items are in ingredients array
    if i in ingredients:

      # If so, divide ingredients numbers by recipes numbers
      current_total = ingredients[i] // recipe[i]
      print("current totals", current_total)

      if total == None:
        total = current_total
        print("total:", total)

      elif total > current_total:
        total = current_total
    else:
      return 0
  
  return total

print(recipe_batches(
  { 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 }
))

# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test 
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))