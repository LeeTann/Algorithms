#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

# 0(n) - Linear - when using memcache. 
# 0(3^n) - Exponential Time - when not using memcache since it calles recursion function 3 times

# For memchache you usually want to implement a dict outside the function
# For the dict then, memchase[n] would be the key, outcome would be value
memcache = {}

def eating_cookies(n, memcache=None):
  # check if memcache has a value first, if it does we can just return
  if n in memcache:
    # memcache[n] is every value thats been called before
    return memcache[n]

  if n < 0:
    return -1
  if n <= 1:
    return 1
  if n == 2:
    return 2

  # calculate 
  output = int(eating_cookies(n-1, memcache) + eating_cookies(n-2, memcache) + eating_cookies(n-3, memcache)) # O(3^n).
  memcache[n] = output
  print("memcache", memcache)
  return output

print(eating_cookies(10, memcache))
print(memcache)

# if __name__ == "__main__":
#   if len(sys.argv) > 1:
#     num_cookies = int(sys.argv[1])
#     print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
#   else:
#     print('Usage: eating_cookies.py [num_cookies]')