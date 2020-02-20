#!/usr/bin/python

import sys

def rock_paper_scissors(rounds):
  # rock = ['rock']
  # paper = ['paper']
  # scissors = ['scissors']
  plays = [['rock'], ['paper'], ['scissors']]
  results = []

  for i in range(0, rounds):
    current_results = []
    for j in range(0, rounds):
      current_results += plays[j]
    results.append(current_results)


  return results 

print(rock_paper_scissors(3))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')