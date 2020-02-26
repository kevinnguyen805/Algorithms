#!/usr/bin/python

import sys


def rock_paper_scissors(rounds):
  def get_plays(round):
    result = []
    moves = [['rock'],['paper'],['scissors']]

    for play in round:
      for move in moves:
        result.append(play + move)
    
    return result
  
  if rounds == 0:
    return [[]]
  if rounds == 1:
    return [['rock'],['paper'],['scissors']]
  
  return get_plays(rock_paper_scissors(rounds-1))


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')