import heapq # q:queue队列，优先队列
import random

# 生成随机list，有两种方式
# 1、random.randint
# li = [random.randint(0, 50) for i in range(20)]
# 2、生成排序list后打乱
li = list(range(20))
random.shuffle(li)
print(li)
heapq.heapify(li) # 建堆（小根堆）
print(li)
for i in range(len(li)):
  # heapq.heappop每次会弹出一个最小的数
  print(heapq.heappop(li), end=",")
  # 可以看到相对应的list会改变，不断减少一个最小值
  print(li)
  # 与之相对的是heapq.heappush(heap, item),插入值


