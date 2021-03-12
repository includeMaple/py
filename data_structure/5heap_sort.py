import random
# 堆的向下调整
def heap_low(li, low, high):
  temp = li[low]
  # 当low和high相等时，停止循环
  while low < high:
    # 下面要分类有两种分类方式：
    # 1、先考虑只有左孩子的情况，再考虑右孩子的情况，每种情况再分开考虑
    # 2、实际只有两种情况，右边孩子和temp交换，左边孩子和temp交换
    # 第一种方式比较直观，但代码冗长，第二种方式不直观，但代码简单，注视是第一种情况
    # if 2 * low + 1 == high:
    #   if li[low] < li[2*low+1]:
    #     li[low] = li[2*low+1]
    #     low = 2*low+1
    #   else:
    #     break
    # # 有俩孩子
    # elif 2 * low + 2 <= high:
    #   # 俩孩子都比她大
    #   if li[low] < li[2*low+1] and li[low] < li[2*low+2]:
    #     if li[2*low+1] < li[2*low+2]:
    #       li[low] = li[2*low+2]
    #       low = 2*low+2
    #     else:
    #       li[low], li[2*low+1] = li[2*low+1], li[low]
    #       low = 2*low+1
    #   # 只有右孩子比她大
    #   elif li[low] < li[2*low+2]:
    #     li[low] = li[2*low+2]
    #     low = 2*low+2
    #   # 只有左孩子比她大
    #   elif li[low] < li[2*low+1]:
    #     li[low] = li[2*low+1]
    #     low = 2*low+1
    #   else:
    #     break
    # 右边孩子上位情况,只有一种可能，满足
    # 1、存在右边孩子
    # 2、右边孩子比左边孩子大
    # 3、右边孩子比temp大
    if low*2+2<=high and li[low*2+2]>li[low*2+1] and li[low*2+2]>temp:
      li[low] = li[low*2+2]
      low = low*2+2
    # 左边孩子上位，并且排除上面情况
    elif low*2+1<=high and li[low*2+1] > temp:
      li[low] = li[low*2+1]
      low = low*2+1
    else:
      break
    li[low] = temp
    # print(li)
  return li

# 堆挨个出数
def heap_one_by_one(li):
  low = 0
  # high = len(li) - 1
  # while low < high:
  #   li[low], li[high] = li[high], li[low]
  #   high -= 1
  #   li = heap_low(li, low, high)
  for high in range(len(li)-1, -1, -1):
    li[low], li[high] = li[high], li[low]
    li = heap_low(li, low, high-1)
  return li

# 建立堆，建立堆是从底部开始的
def heap_create(li):
  n = len(li) - 1
  # 循环所有根节点
  for i in range((n-2+1)//2, -1, -1):
    li = heap_low(li, i, n)
  return li

def heap_sort(li):
  # 1、建立堆
  li = heap_create(li)
  print(li)
  # 2、挨个出数
  li = heap_one_by_one(li)
  return li

# li = [3, 8, 7, 6, 5, 0, 1, 2, 4]
# li = heap_low(li, 0, len(li)-1)
# print(li)
print('-----------------start------------------')
li = [random.randint(0, 100) for i in range(6)]
print(li)
print(heap_sort(li))
print('--------------------end--------------')
