class Node:
  def __init__(self, item=None):
    self.data = item
    self.lchild = None
    self.rchild = None
    self.parent = None

class SearchTree:
  def __init__(self, li=None):
    self.root = None
    if li:
      self.root = Node(li[0])
      for i in range(1, len(li)):
        self.insert_ord(li[i])
  # 递归是无法插入的吧，视频的代码一定是错误的，我自己弄了半天烦死了还是没调通
  # 视频里不是递归插入方式其实也有问题
  # 以下代码代码执行会递归修改复写内容
  # def insert_rec(self, item, node='default'):
  #   if node == 'default'and not self.root:
  #     self.root = Node(item)
  #   if node == 'default':
  #     node = self.root
  #   if node:
  #     if node.data > item:
  #       self.insert_rec(item, node.lchild)
  #       new_node = Node(item)
  #       node.lchild = new_node
  #       new_node.parent = node
  #     elif node.data < item:
  #       self.insert_rec(item, node.rchild)
  #       new_node = Node(item)
  #       node.rchild = new_node
  #       new_node.parent = node
  #       return
  #     else:
  #       print('this is dupcilte')

  def insert_ord(self, item):
    p = self.root
    if not p: # empty tree
      self.root = Node(item)
      return
    while True:
      if item < p.data:
        if p.lchild:
          p = p.lchild
        else:
          p.lchild = Node(item)
          p.lchild.parent = p
          return
      elif item > p.data:
        if p.rchild:
          p = p.rchild
        else:
          p.rchild = Node(item)
          p.rchild.parent = p
          return
      else:
        return
  
  def delete1(self, item):
    cur_node = self.find_node(item)
    if not cur_node: # 不需要删除
      return False
    # 没有孩子是叶子结点
    elif not cur_node.lchild and not cur_node.rchild:
      self.delete_leaf(cur_node)
    # 只有一个孩子
    elif not cur_node.lchild or not cur_node.rchild:
      self.delete_one_child(cur_node)
    # 有俩孩子
    else:
      find_node = cur_node.rchild
      while find_node.lchild:
        find_node = find_node.lchild
      # 这里没有对节点进行移动，而是改变了data，也就是里面的值，delete里一直在移动
      cur_node.data = find_node.data
      # 然后删除node
      if find_node.rchild:
        self.delete_one_child(find_node)
      else:
        self.delete_leaf(find_node)


  
  # node节点是叶子结点的删除
  def delete_leaf(self, node):
    # 只有一个节点，是根节点的情况
    if node.parent == None:
      self.root = None
      return
    if node == node.parent.lchild:
      node.parent.lchild = None
    else:
      node.parent.rchild = None
    
  # 节点只有一个孩子
  def delete_one_child(self, node):    
    if node.lchild:
      if not node.parent:
        self.root = node.lchild
        node.lchild.parent = None
        return
      node.lchild.parent = node.parent
      if node == node.parent.lchild:
        node.parent.lchild = node.lchild
      else:
        node.parent.rchild = node.lchild
    else:
      if not node.parent:
        self.root = node.rchild
        node.rchild.parent = None
        return
      node.rchild.parent = node.parent
      if node == node.parent.lchild:
        node.parent.lchild = node.rchild
      else:
        node.parent.rchild = node.rchild


  def delete(self, item):
    cur_node = self.find_node(item)
    if cur_node:
      # 叶子节点
      if not cur_node.lchild and not cur_node.rchild:
        if not cur_node.parent:
          self.root = None
        else:
          if cur_node.parent.lchild == cur_node:
            cur_node.parent.lchild = None
            cur_node.parent = None
          else:
            cur_node.parent.rchild = None
            cur_node.parent = None
      # 只有右孩子
      elif not cur_node.lchild and cur_node.rchild:
        if not cur_node.parent:
          self.root = cur_node.rchild
        elif cur_node == cur_node.parent.lchild:
          cur_node.parent.lchild = cur_node.rchild
          cur_node.rchild.parent = cur_node.parent
        else:
          cur_node.parent.rchild = cur_node.rchild
          cur_node.rchild.parent = cur_node.parent
      # 只有左孩子
      elif cur_node.lchild and not cur_node.rchild:
        if not cur_node.parent:
          self.root = cur_node.lchild
          cur_node.parent = None
        elif cur_node == cur_node.parent.lchild:
          cur_node.parent.lchild = cur_node.lchild
          cur_node.lchild.parent = cur_node.parent
        else:
          cur_node.parent.rchild = cur_node.lchild
          cur_node.lchild.parent = cur_node.parent
      # 有俩孩子，但是右边孩子没有左孩子, 右孩子上移动
      elif cur_node.lchild and cur_node.rchild and not cur_node.rchild.lchild:
        if not cur_node.parent:
          cur_node.rchild.lchild = self.root.lchild
          self.root = cur_node.rchild          
        elif cur_node == cur_node.parent.lchild:
          cur_node.rchild.lchild = cur_node.lchild
          cur_node.lchild.parent = cur_node.rchild
          cur_node.rchild.parent = cur_node.parent
          cur_node.parent.lchild = cur_node.rchild
        else:
          cur_node.rchild.lchild = cur_node.lchild
          cur_node.lchild.parent = cur_node.rchild
          cur_node.rchild.parent = cur_node.parent
          cur_node.parent.rchild = cur_node.rchild
      # 有俩孩子
      # 1 找到右子树的最小节点 
      # 2 有两种情况，其一有右孩子，其二没有右孩子
      # 3 将其移动到当前位置
      else:
        # 1 找到right true的left最小节点
        find_node = cur_node.rchild
        while find_node.lchild:
          find_node = find_node.lchild
        # 2 节点情况1：没有右孩子，直接把这个点移上来
        if not find_node.rchild:
          find_node.parent.lchild = None
        # 2 节点情况2：有右孩子
        else:
          find_node.rchild.parent = find_node.parent
          find_node.parent.lchild = find_node.rchild
        find_node.lchild = cur_node.lchild
        cur_node.lchild.parent = find_node
        find_node.rchild = cur_node.rchild
        cur_node.rchild.parent = find_node
        find_node.parent = cur_node.parent
        if cur_node == cur_node.parent.lchild:
          cur_node.parent.lchild = find_node
        else:
          cur_node.parent.rchild = find_node

      
          
  def find_node(self, item):
    cur_node = self.root
    # 确保node有孩子，不管是左孩子还是右孩子
    while cur_node:
      if cur_node.data == item:
        return cur_node
      elif cur_node.data > item:
        cur_node = cur_node.lchild
      else:
        cur_node = cur_node.rchild
    return False

  def find(self, item):
    cur_node = self.root
    # 确保node有孩子，不管是左孩子还是右孩子
    while cur_node:
      if cur_node.data == item:
        return True
      elif cur_node.data > item:
        cur_node = cur_node.lchild
      else:
        cur_node = cur_node.rchild
    return False

  # 前序遍历
  def pre_every(self, node):
    if node: # 如果节点不为空
      print(node.data, end=", ")
      self.pre_every(node.lchild)
      self.pre_every(node.rchild)

  # 中序遍历
  def mid_every(self, node):
    if node:
      self.mid_every(node.lchild)
      print(node.data, end=", ")
      self.mid_every(node.rchild)

  # 后序便利
  def back_every(self, node):
    if node:
      self.back_every(node.lchild)
      self.back_every(node.rchild)
      print(node.data, end=", ")

# tree = SearchTree([5, 2, 6, 3, 4, 1])
# tree.insert_ord(10)
# tree.insert_ord(12)
# print('\npre_every')
# tree.pre_every(tree.root)
# print('\nmid_every')
# tree.mid_every(tree.root)
# print('\nback_every')
tree = SearchTree([5, 2, 10, 3, 4, 1, 6, 20, 22,15,0])
tree.mid_every(tree.root)
tree.delete1(5)
print('---')
tree.mid_every(tree.root)