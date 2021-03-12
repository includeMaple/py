import random
# 堆的向下调整
def heap_low(li, low, high, isLarge=True):
  temp = li[low]
  # 当low和high相等时，停止循环
  while low < high:
    if isLarge:
      if low*2+2<=high and li[low*2+2]>li[low*2+1] and li[low*2+2]>temp:
        li[low] = li[low*2+2]
        low = low*2+2
      # 左边孩子上位，并且排除上面情况
      elif low*2+1<=high and li[low*2+1] > temp:
        li[low] = li[low*2+1]
        low = low*2+1
      else:
        break
    else:
      if low*2+2<=high and li[low*2+2]<li[low*2+1] and li[low*2+2]<temp:
        li[low] = li[low*2+2]
        low = low*2+2
      # 左边孩子上位，并且排除上面情况
      elif low*2+1<=high and li[low*2+1] < temp:
        li[low] = li[low*2+1]
        low = low*2+1
      else:
        break
    li[low] = temp
    # print(li)
  return li

# 堆挨个出数
def heap_one_by_one(li, isLarge=True):
  low = 0
  for high in range(len(li)-1, -1, -1):
    li[low], li[high] = li[high], li[low]
    li = heap_low(li, low, high-1, isLarge)
  return li

# 建立堆，建立堆是从底部开始的
def heap_create(li, isLarge=True):
  n = len(li) - 1
  # 循环所有根节点
  for i in range((n-2+1)//2, -1, -1):
    li = heap_low(li, i, n, isLarge)
  return li

# topk问题
def top_sort(li, k, isLarge=True):
  # 1、建立k个数的堆
  li_topk = li[0: k]
  heap_create(li, isLarge)
  print(li_topk)
  # 2、遍历剩下的所有数
  for i in range(k, len(li)-1):
    # 判断循环出的数和小根堆top的大小
    if li[i] > li_topk[0]:
      li_topk[0] = li[i]
      heap_low(li_topk, 0, len(li_topk)-1, False)
      # print(li_topk)
  return li_topk

# 堆排序
def heap_sort(li, isLarge=True):
  # 1、建立堆
  heap_create(li, isLarge)
  print('create heap')
  print(li)
  # 2、挨个出数
  heap_one_by_one(li, isLarge)

# li = [3, 8, 7, 6, 5, 0, 1, 2, 4]
# li = heap_low(li, 0, len(li)-1)
# print(li)
print('-----------------start------------------')
li = [random.randint(0, 100) for i in range(10)]
print(li)
# heap_sort(li, False)
print(top_sort(li, 5, False))
# print(li)
print('--------------------end--------------')
