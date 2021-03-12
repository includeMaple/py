import random

def bucket_sort(li, max, n=5):
  temp = [[] for i in range(n)]
  for val in li:
    i = min(val//(max//n), n-1) # i表示是哪个桶
    temp[i].append(val)
    for j in range(len(temp[i])-1, 0, -1):
      if temp[i][j] < temp[i][j-1]:
        temp[i][j], temp[i][j-1] = temp[i][j-1], temp[i][j]
      else:
        break
  sort_li = []
  for t in temp:
    sort_li.extend(t)
  return sort_li

li = [random.randint(1, 100) for i in range(20)]
print(li)
print(bucket_sort(li, 100))


