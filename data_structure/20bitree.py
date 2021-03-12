from collections import deque
class BiTreeNode:
  def __init__(self, data):
    self.data = data
    self.lchild = None
    self.rchild = None

# 手写二叉树
e = BiTreeNode('E')
a = BiTreeNode('A')
g = BiTreeNode('G')
c = BiTreeNode('C')
f = BiTreeNode('F')
b = BiTreeNode('B')
d = BiTreeNode('D')
e.lchild = a
e.rchild = g
a.rchild = c
g.rchild = f
c.lchild = b
c.rchild = d

root = e
print(root.lchild.data)

# 前序遍历
def pre_every(node):
  if node: # 如果节点不为空
    print(node.data, end=", ")
    pre_every(node.lchild)
    pre_every(node.rchild)
print('pre_every')
pre_every(root)

# 中序遍历
def mid_every(node):
  if node:
    mid_every(node.lchild)
    print(node.data, end=", ")
    mid_every(node.rchild)
print('\nmid_every')
mid_every(root)

# 后序便利
def back_every(node):
  if node:
    back_every(node.lchild)
    back_every(node.rchild)
    print(node.data, end=", ")
print('\nback_every')
back_every(root)

def lev_every(node):
  q = deque()
  q.append(node)
  while len(q) > 0:
    cur_node = q.popleft()
    print(cur_node.data, end='_')
    if cur_node.lchild:
      q.append(cur_node.lchild)
    if cur_node.rchild:
      q.append(cur_node.rchild)
print('\nlevel every')
lev_every(root)






