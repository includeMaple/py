import random

def merge(li, lstart, lend, rstart, rend, positive=True):
  start = lstart
  end = rend
  temp = []
  while lstart<= lend and rstart <= rend:
    if positive:
      if li[lstart] < li[rstart]:
        temp.append(li[lstart])
        lstart += 1
      else:
        temp.append(li[rstart])
        rstart += 1
    else:
      if li[lstart] > li[rstart]:
        temp.append(li[lstart])
        lstart += 1
      else:
        temp.append(li[rstart])
        rstart += 1
  if lstart <= lend:
    for i in range(lstart, lend+1):
      temp.append(li[i])
  else:
    for i in range(rstart, rend+1):
      temp.append(li[i])
  li[start: end+1] = temp

def merge_sort(li, start, end):
  if start < end: # 确保至少有2个元素
    mid = (start+end)//2
    merge_sort(li, start, mid)
    merge_sort(li, mid+1, end)
    merge(li, start, mid, mid+1, end)
    # print('start: %s, end: %s, mid: %s ' %(start, end, mid))
    print(li)


li = [random.randint(0,100) for i in range(10)]
print(li)
# merge(li, 0, 0, 1, 1)
merge_sort(li, 0, 9)
print(li)