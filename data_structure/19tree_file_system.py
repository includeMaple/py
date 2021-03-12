
class Node:
  def __init__(self, name, type="dir"):
    self.name = name
    self.type = type
    self.children = []
    self.parent = None


class FileSystemTree:
  def __init__(self):
    self.root = Node("/")
    self.now = self.root

  def mkdir(self, name):
    if name[-1] != '/':
      name += '/'
    node = Node(name)
    self.now.children.append(node)
    node.parent = self.now

  def ls(self):
    str1 = ''
    for i in self.now.children:
      str1 += str(i.name)
      str1 += " "
    return str1

  def cd(self, name):
    if name[-1] != '/':
      name += '/'
    if name == "../":
      self.now = self.now.parent
      return
    for child in self.now.children:
      if child.name == name:
        self.now = child
        return True
    raise ValueError('invalid dir')

tree = FileSystemTree()
tree.mkdir("var/")
tree.mkdir("bin/")
tree.mkdir("usr/")
tree.cd("bin/")
tree.cd("../")
tree.mkdir("name")
print(tree.ls())
