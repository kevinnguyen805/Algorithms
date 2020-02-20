#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(target, cache=None): 
  cache = {}

  def recursion(target, cache):
    if target in cache:
      return cache[target]
    
    if target < 0:
      return 0
    elif target == 0: 
      return 1
    elif target == 1:
      return 1
    else:
      result = recursion(target-1, cache) + recursion(target-2, cache) + recursion(target-3, cache)
      cache[target] = result 
      return result 
  
  return recursion(target, cache)




if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')