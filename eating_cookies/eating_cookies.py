#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
# def eating_cookies(n): 
#   numbers = [1,2,3]
#   remaining = len(numbers)
#   cookie_count = 0

#   for i in range(0, len(numbers)):
#     current_total = []
#     if sum(current_total) == n:
#         cookie_count += 1

#     for j in range(0, len(numbers)):
  







if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')