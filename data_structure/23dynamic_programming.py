# 斐波那切数列，第n项
def fibnacci_rec(n):
  if n > 1:
    return fibnacci_rec(n-1)+fibnacci_rec(n-2)
  else:
    return 1
    
def fibnacci_ord(n):
  temp = [1, 1]
  for i in range(2, n+1):
    temp.append(temp[-1] + temp[-2])
  return temp[-1]

print(fibnacci_rec(10))
print(fibnacci_ord(10))

# 钢条切割问题，普通方法
def cut_steel(n,li):
  temp = [li[0]]
  for i in range(1, n+1):
    one_max = None
    for j in range(min(i, len(li) - 1)):
      t = li[j] + li[i-j]
      if not one_max or one_max<t:
        one_max = t
    temp.append(one_max)
  return temp[n]

# 钢条切割问题，递归（以前的递归）
def cut_steel_rec1(n, li):
  if n == 0:
    return 0
  else:
    temp = li[n]
    for i in range(1, n):
      temp = max(temp, cut_steel_rec1(i, li) + cut_steel_rec1(n-i, li))
    return temp

# 优化钢条切割问题，递归
def cut_steel_rec2(n, li):
  if n == 0:
    return 0
  else:
    for i in range(1, n+1):
      temp = max(li[i], li[i-1] + cut_steel_rec2(n-i, li))
    li[n] = temp
    return temp
      

# 这是钢条切割问题的价格表，下标表示切割长度，值表示这个长度的价值
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n=10
print(cut_steel(n, p))
print('----')
print(cut_steel_rec1(n, p))
print(cut_steel_rec2(n, p))

# 修改切割方式
def cut_steel_rec6(n,li):
  temp = [li[0]]
  res_li_s = [0]
  for i in range(1, n+1):
    res_s = 0
    one_max = None
    for j in range(min(i, len(li) - 1)):
      t = li[j] + li[i-j]
      if not one_max or one_max<t:
        one_max = t
        res_s = j
    temp.append(one_max)
    res_li_s.append(res_s)
  print(res_li_s)
  return temp, res_li_s

def get_cut(cut_li, n):
  temp = []
  if cut_li[n] == 0:
    temp.append(0)
  while cut_li[n] > 0:
    temp.append(cut_li[n])
    n = n - cut_li[n]
  temp.append(n)
  return temp

p1= [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
n1=10
max_num, li = cut_steel_rec6(n1, p1)
print(max_num)
print(li)
print(get_cut(li, 3))
print('----000--')
