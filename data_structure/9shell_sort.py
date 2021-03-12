import random

def insert_sort(li, step=1, positive=True):
  # i是抽到的牌，对比时从i-1张牌往前数到第0张牌
  for i in range(1, len(li)):
    temp = li[i]
    j = i-step
    if positive:
      while j>=0 and temp<li[j]:
        li[j+step] = li[j]
        j -= step
      li[j+step] = temp
    else:
      while j>=0 and temp>li[j]:
        li[j+step] = li[j]
        j -= step
      li[j+step] = temp

def shell_sort(li, positive=True):
  step = len(li)//2
  while step>0:
    print(li)
    insert_sort(li, step, positive)
    step //= 2

li = [random.randint(0, 100) for i in range(10)]
print(li)
shell_sort(li)
print(li)