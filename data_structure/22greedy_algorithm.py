
# 找钱问题，或者给钱问题，size直接是倒叙排列，不是的话，可以排完序再传入使用
def give_money(num, size=[100, 50, 20, 10, 5, 1]):
  temp = []
  for i in range(len(size)):
    n = num // size[i]
    if n > 0:
      temp.append(n)
      num %= size[i]
  return temp

money = 383
print(give_money(money))

# 分数背包
def back1(w, value):
  temp = []
  for item in value:
    if item[1]>=w:
      temp.append(w)
      w = 0
    else:
      temp.append(item[1])
      w -= item[1]
  return temp

# 下面比如60分别代表总价值和总重量
li = [[60, 10], [100, 20], [120, 30]]
li.sort(key = lambda x: x[0]/x[1])
print(li)
print(back1(10, li))

# 拼接最大数字问题
def max_num(li):
  li.sort(reverse=True)
  print(li)
  for i in range(len(li)-1):
    if li[i].startswith(li[i+1]) or li[i+1].startswith(li[i]):
      if int(li[i]+li[i+1]) < int(li[i+1]+li[i]):
        li[i], li[i+1] = li[i+1], li[i]

li = ['2231', '223', '34', '02']
max_num(li)
print(li)

def xy_cmp(x, y):
  if x+y < y+x:
    return 1
  elif x+y > y+x:
    return -1
  else:
    return 0
from functools import cmp_to_key
def max_num1(li):
  li = list(map(str, li))
  # 这里的排序原理，前后相减，如果是负数则交换，
  li.sort(key=cmp_to_key(xy_cmp))
  return ''.join(li)

li = [2231, 223, 34, 2]
print(max_num1(li))

# 活动选择问题
def choose_time(li):
  res = [li[0]]
  for i in range(1, len(li)):
    # 当前的开始时间大于等于最后一个元素(已经入选活动)的结束时间，表示不冲突
    if li[i][0] >= res[-1][1]:
      res.append(li[i])
  return res

li = [(1, 4), (3, 5), (2, 7), (4, 5), (5,9), (6, 9), (7, 10)]
li.sort(key=lambda x:x[1])
print(li)
print(choose_time(li))

