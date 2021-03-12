import log
from fun_time import *

@func_time
def linear_search(li, val):
  for ind, value in enumerate(li):
    if value == val:
      return ind
  return None

@func_time
def binary_search(li, val):
  left = 0
  right = len(li) - 1
  while left <= right and val >= li[left] and val <= li[right]:
    mid = (left+right) // 2
    if li[mid] == val:
      return 'index:%s, value: %s' % (mid, val)
    elif li[mid] > val:
      right = mid - 1
    else:
      left = mid + 1
  return None

l = range(10000)
binary_search(l, 999)
linear_search(l, 999)