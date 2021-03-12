from collections import deque

def next_node(maze, x, y):
  temp = []
  if x > 0 and maze[x-1][y] == 0:
    temp.append([x-1, y])
  if y < len(maze) - 1 and maze[x][y+1] == 0:
    temp.append([x, y+1])
  if x < len(maze) - 1 and maze[x+1][y] == 0:
    temp.append([x+1, y])
  if y > 0 and maze[x][y-1] == 0:
    temp.append([x, y-1])
  return temp

def print_path(path):
  temp=[]
  i=len(path)-1
  temp.append(path[i][0])
  while i>0:
    i=path[i][1]
    temp.append(path[i][0])
  for i in range(len(temp)-1, -1, -1):
    print(temp[i])
  # print(temp.reverse())

def maze_queue(maze, start=[1,1], end=[8,8]):
  # 使用list存储前后节点的位置
  path = []
  # 使用队列存储下一步能走的所有位置，联系上一节点的方法是多一个参数存储位置
  q = deque()
  q.append([start, -1])
  # 只要队列里有内容，如果没内容，说明结束了
  while len(q) > 0:
    # 遍历每个点能走到下个点的全部进队列，并且存储temp确定其上一node是什么
    cur_node_info = q.popleft()
    path.append(cur_node_info)
    cur_node=cur_node_info[0]
    if cur_node == end:
      print_path(path)
      return True
      # print(path)
    next_nodes = next_node(maze, cur_node[0], cur_node[1])
    for j in range(len(next_nodes)):
      q.append([next_nodes[j], len(path) - 1])
      # 走多地点标记为2
      maze[next_nodes[j][0]][next_nodes[j][1]] = 2
  return False

maze = [
  [1,1,1,1,1,1,1,1,1,1],
  [1,0,0,1,0,0,0,1,0,1],
  [1,0,0,1,0,0,0,1,0,1],
  [1,0,0,0,0,1,1,0,0,1],
  [1,0,1,1,1,0,0,0,0,1],
  [1,0,0,0,1,0,0,0,0,1],
  [1,0,1,0,0,0,1,0,0,1],
  [1,0,1,1,1,0,1,1,0,1],
  [1,1,0,0,0,0,0,0,0,1],
  [1,1,1,1,1,1,1,1,1,1]
]
maze_queue(maze)