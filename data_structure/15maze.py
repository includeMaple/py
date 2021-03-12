
# 顺序确定就行，不一定需要上右下左，这里矩阵x是y，y是x
def get_next(maze, x, y):
  if x > 0 and maze[x-1][y] == 0:
    return [x-1, y]
  if y < len(maze) - 1 and maze[x][y+1] == 0:
    return [x, y+1]
  if x < len(maze) - 1 and maze[x+1][y] == 0:
    return [x+1, y]
  if y > 0 and maze[x][y-1] == 0:
    return [x, y-1]
  return False

def maze_heap(maze, start=[1, 1], end=[8, 8]):
  stack = []
  stack.append(start)
  maze[start[0]][start[1]] = 2
  while len(stack) > 0:
    next_point = get_next(maze, start[0], start[1])
    # 没有找到下一个点需要出栈
    if not next_point:
      stack.pop()
      start = stack[len(stack) - 1]
    elif next_point == end: # 出迷宫
      stack.append(next_point)
      return stack
    else:
      stack.append(next_point)
      maze[next_point[0]][next_point[1]] = 2
      start = next_point
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

print(maze_heap(maze))

  
