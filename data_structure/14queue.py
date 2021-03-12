from collections import deque

q = deque()
# 队尾进队，队首出队
q.append(1)
q.popleft()
# 队首进队，队尾出队
q.appendleft(2)
q.pop()

# 创建队列，上面没有传递任何值创建了一个空队列，也可以如下
q1 = deque([1,3,4])
# 第二个参数是最大长度，上面简单代码实现的单向队列队满再进队是提示，这里是自动出队一个
q2 = deque([1,3,4,5,6], 5)
q2.append(9)
print(q2.popleft())



def tail(n):
  print('----')
  f = open('test.txt', 'r')
  q = deque(f, n)
  return q
  # with open('test.txt', 'r') as f

print(tail(5))

