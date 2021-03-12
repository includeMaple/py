import random
from fun_time import *

@func_time
def bubble_sort(li, positive=True):
  for i in range(len(li)-1):
    isSort = False
    for j in range(len(li)-i-1):
      if positive:
        if li[j] > li[j+1]:
          li[j], li[j+1] = li[j+1], li[j]
          isSort = True
      else:
        if li[j] < li[j+1]:
          li[j], li[j+1] = li[j+1], li[j]
          isSort = True
    if not isSort:
      return li
  return li

@func_time
def select_sort(li, positive=True):
  for i in range(len(li)-1):
    if positive:
      min_local = i
      for j in range(i+1, len(li)):
        if li[min_local] > li[j]:
          min_local = j
      # 每循环一趟，找到一个最小值的下标，然后交换一次
      li[i], li[min_local] = li[min_local], li[i]
    else:
      max_local = i
      for j in range(i+1, len(li)):
        if li[max_local] < li[j]:
          max_local = j
      li[i], li[max_local] = li[max_local], li[i]
  return li

# insert_sort中这个比较快
@func_time
def insert_sort2(li, positive=True):
  # i是抽到的牌，对比时从i-1张牌往前数到第0张牌
  for i in range(1, len(li)):
    temp = li[i]
    j = i-1
    if positive:
      while j>=0 and temp<li[j]:
        li[j+1] = li[j]
        j = j-1
      li[j+1] = temp
    else:
      while j>=0 and temp>li[j]:
        li[j+1] = li[j]
        j = j-1
      li[j+1] = temp
  return li

# 这是我一开始写的，但其实这种方式不好，又慢又不要理解，保存在这里只是保存下，插入排序用上面方法
@func_time
def insert_sort3(li, positive=True):
  # i是抽到的牌，对比时从0张牌往后数到第i-1张牌
  for i in range(1, len(li)):
    for j in range(i):
      isBegin = False
      if positive:
        if li[j] > li[i]:
          temp = li[j]
          li[j] = li[i]
          isBegin = True
        elif isBegin:
          li[j], temp = temp, li[j]
      else:
        if li[j] < li[i]:
          temp = li[j]
          li[j] = li[i]
          isBegin = True
        elif isBegin:
          li[j], temp = temp, li[j]
  return li

# 随机生成10000个[0，100000]之间的随机数，并用shuffle打乱
li = [random.randint(0, 100000) for i in range(10000)]
random.shuffle(li)

print('-------------start--------------')
# bubble_sort(li)
# select_sort(li)
insert_sort2(li)
insert_sort3(li)
print('--------------end---------------')


