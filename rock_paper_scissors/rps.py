#!/usr/bin/python

# Need to get all possible permutation. recursion is the way to go.
# we have 3 choices = rock, paper, scissors

import sys

def rock_paper_scissors(n):
  outcomes = []
  choices = ["rock", "paper", "scissors"]

  # Create a recursive to help get results
  def get_result(rounds, arr=[]):
    
    # Base case - if rounds is 0, add the arr to outcomes
    if rounds == 0:
      new_outcomes = outcomes.append(arr)
      return new_outcomes 

    # else loop thru all the choices and keep recursing down the function by rounds -1, adding list arr with each_choice  
    else:
      for each_choice in choices:
        get_result(rounds -1, arr + [each_choice]) # can only concatenate list to list, not list to str so put each_choice in []

  # call the helper function  
  get_result(n, [])
  
  # return outcomes
  return outcomes

print(rock_paper_scissors(3))

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_plays = int(sys.argv[1])
#     print(rock_paper_scissors(num_plays))
#   else:
#     print('Usage: rps.py [num_plays]')