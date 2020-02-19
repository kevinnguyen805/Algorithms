#!/usr/bin/python

import argparse

def find_max_profit(prices):
  buy = prices[0]
  profits = prices[1] - prices[0]

  for i in range(1, len(prices)):
    if buy > prices[i]:
      buy = prices[i]
    else: 
      current_profits = prices[i]- buy
      profits = max(profits, current_profits)
  return profits


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))