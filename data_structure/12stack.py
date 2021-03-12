

class Stack:
  def __init__(self):
    self.stack = []
  
  def push(self, element):
    self.stack.append(element)
  
  def pop(self):
    return self.stack.pop()

  def get_top(self):
    if len(self.stack)>0:
      return self.stack[-1]
    else:
      return None

  def is_empty(self):
    return len(self.stack) == 0

def match(str1):
  stack = Stack()
  li = ['[', ']', '{', '}', '(', ')']
  for i in range(len(str1)):
    ind = li.index(str1[i])
    if ind % 2 == 0:
      stack.push(str1[i])
    else:
      if stack.is_empty():
        return False
      if stack.pop() != li[ind-1]:
        return False
  if stack.is_empty():
    return True
  return False
    
# stack = Stack()
str1 = '}'
print(match(str1))

