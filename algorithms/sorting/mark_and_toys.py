#!/usr/bin/env python

def max_toys(prices, rupees):
  #Compute and return final answer over here
  list.sort(prices)
  answer = 0
  for x in prices:
        if x < rupees:
            rupees -= x
            answer += 1
  return answer

if __name__ == '__main__':
  n, k = map(int, raw_input().split())
  prices = map(int, raw_input().split())
  print max_toys(prices, k)
