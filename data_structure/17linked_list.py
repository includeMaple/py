class Node(object):
  def __init__(self, item):
    self.item = item
    self.next = None

a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
print(a.next.item) # 2
print(a.next.next.item) # 3
# 创建链表，头插法
def create_linklist_head(li):
  head = Node(li[0])
  for el in li[1:]:
    new_node = Node(el)
    new_node.next = head
    head = new_node
  return head

# 创建链表，尾插法，尾插法比头插法多维护一个tail
def create_linklist_tail(li):
  head = Node(li[0])
  tail = head
  for el in li[1:]:
    new_node = Node(el)
    tail.next = new_node
    tail = new_node
  return head

# 打印链表
def print_linklist(lk):
  while lk:
    print(lk.item, end=',')
    lk = lk.next

lk = create_linklist_head([1,3,4,5,5,8]) #8,5,5,4,3,1,
print_linklist(lk)
lk = create_linklist_tail([1,3,4,5,5,8]) #1,3,4,5,5,8,
print_linklist(lk)

