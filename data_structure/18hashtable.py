
# 链表链
class Linklist:
  # node节点
  class Node:
    def __init__(self, item = None):
      self.item = item
      self.next = None
  
  class LinklistIterator:
    def __init__(self, node):
      self.node = node

    def __next__(self):
      if self.node:
        cur_node = self.node
        self.node = cur_node.next
        return cur_node.item
      else:
        raise StopIteration
    
    def __iter__(self):
      return self

  # 构造函数，允许传递一个列表进来，将列表变成链表
  def __init__(self, iterable=None):
    self.head = None
    self.tail = None
    if iterable:
      self.extend(iterable)
  
  def append(self, obj):
    s = Linklist.Node(obj)
    if not self.head:
      self.head = s
      self.tail = s
    else:
      self.tail.next = s
      self.tail = s

  def extend(self, iterable):
    for obj in iterable:
      self.append(obj)

  # 查找，是否能查到
  def find(self, obj):
    for n in self:
      if n == obj:
        return True
      else:
        return False
  
  # 让链表支持迭代器，所以可以使用for循环
  def __iter__(self):
    return self.LinklistIterator(self.head)
  # 打印的时候可以直接打印
  def __repr__(self):
    return "<<" + ", ".join(map(str, self)) + ">>"

# 下面是链表的测试代码，请勿删除
# lk = Linklist([1,3,4,5,6,7])
# for el in lk:
#   print(el)
# print(lk) # <<1, 3, 4, 5, 6, 7>>

# 做一个set的结构，这个结构就不允许重复
class HashTableSet:
  def __init__(self, size=100):
    self.size = size
    # 这里什么都不传存储的是一个空链表
    self.T = [Linklist() for i in range(self.size)]

  # 哈希函数
  def h(self, k):
    return k % self.size

  def insert(self, k):
    # 首先计算哈希值，返回的值是我们要存储的位置
    i = self.h(k)
    # 发现已经有了，则不重复插入
    if self.find(k):
      print('Duplicated insert')
    else:
      self.T[i].append(k)

  def find(self, k):
    i = self.h(k)
    return self.T[i].find(k)

ht = HashTableSet()
ht.insert(0)
ht.insert(1)
ht.insert(0)
ht.insert(100)
ht.insert(101)
# 可以看到打印出来的结果0和100是在一起的，1和101是在一起的
print(', '.join(map(str, ht.T)))