class Queue:
  def __init__(self, size=10):
    self.queue = [0 for i in range(size)]
    self.size = size
    self.front = 0
    self.rear = 0
  
  def isempty(self):
    return self.front == self.rear
  
  def isfull(self):
    return self.len() == self.size - 1

  def len(self):
    if self.rear >= self.front:
      return self.rear - self.front
    else:
      return self.rear+self.size-self.front

  def push(self, element):
    '''
    入队列，首先判断queue是否满，不满的情况下：
    1、next添加新元素
    2、移动front到next
    '''
    if self.isfull():
      print('this queue is full')
    else:
      self.rear = (self.rear + 1) % self.size
      self.queue[self.rear] = element
    
  def pop(self):
    '''
    出队列，首先确认queue是不是空的，非空情况下：
    1、移动rear，不需要其他操作
    '''
    if self.isempty():
      print('this queue is empty')
    else:
      self.front = (self.front + 1) % self.size

queue = Queue(5)
for i in range(10):
  queue.push('sss')
queue.pop()
print(queue.len())

