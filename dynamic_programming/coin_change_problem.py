# Question:
# In this problem you will be given a list of coin denominations and a target amount. 
# Determine the number of ways the target amount can be arrived at using the denominations available.
# We have unlimited supply of coins.

# Source
# https://www.hackerrank.com/challenges/coin-change/problem

#!/bin/python

import sys

def getWays(sum_req, coins):
  coins.sort()
  cost_mat = [[0]*len(coins) for _ in range(sum_req+1)]
  cost_mat[0] = [1]*len(coins) # Sum req=0, all coins has 1 way.

  for s in range(1,sum_req+1):
    for c in range(len(coins)):
      sel_ways = unsel_ways = 0
      if c-1 >=0: # If it is not first coin.
        unsel_ways = cost_mat[s][c-1]
      rem_sum = s-coins[c]
      if rem_sum >=0: # If the value of coin doesn't exceed required sum.
        sel_ways = cost_mat[rem_sum][c]
      cost_mat[s][c] = unsel_ways +sel_ways
  return cost_mat[-1][-1]

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
c = map(long, raw_input().strip().split(' '))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
print ways
