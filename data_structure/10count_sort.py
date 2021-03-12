import random

def count_sort(li, start, end):
  # 生成计数
  temp = [0 for i in range(end-start+1)]
  for i in range(len(li)):
    temp[li[i]-start] += 1
  print(temp)
  # 计数变列表
  li.clear()
  # 虽然这里是双重循环，但是里面循环实际是计数循环，总和最多循环n次，所以这两个复杂度为O(n)
  for ind, val in enumerate(temp):
    for i in range(val):
      li.append(ind+start)

li = [random.randint(-6, 10) for i in range(10)]
print(li)
count_sort(li, -6, 10)
print(li)

