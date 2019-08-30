#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # Keep track of max profit
  min_price = prices[0]
  print("min price = ", min_price)
  max_profit = prices[1] - min_price
  print("max profit = ", max_profit)

  # Loop thru the array with first pointer and get all values
  for i in range(len(prices)):
    print("i varible =", prices[i])

    # Loop thru the array again with second pointer to get second values to compare
    for j in range(i + 1, len(prices)):
      print("j variable", prices[j])

      # Get the difference/current profit which is second pointer minus first pointer
      current_profit = prices[j] - prices[i]
      print("current profit =", current_profit)

      # If current profit > max profit then set max profit = current profit
      if current_profit > max_profit:
        print(f"price_j {prices[j]} - price i {prices[i]}")
        max_profit = current_profit
        print("new max profit = ", max_profit)

  return max_profit
  
print(find_max_profit([1050, 270, 1540, 3800, 2])) 

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))