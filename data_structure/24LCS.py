# 绘制矩阵，获得最长子序列的长度
def lcs_length(x, y):
  m = len(x)
  n = len(y)
  c = [[0 for _ in range(n+1)] for _ in range(m+1)]
  for i in range(1, m+1):
    for j in range(1, n+1):
      # 如果相等，这里的值等于斜上方的值+1
      if x[i-1] == y[j-1]:
        c[i][j] = c[i-1][j-1] + 1
      # 如果不想等，取得上方和左方的最大值
      else:
        c[i][j] = max(c[i-1][j], c[i][j-1])
  for _ in c:
    print(_)
  # 返回最长子序列的长度
  return c[m][n]
lcs_len = lcs_length('ABCBDAB', 'BDCABA')
print(lcs_len)

# 这个打印出了长度并且绘制了矩阵，是上面函数的功能扩充版
def lcs(x, y):
  m = len(x)
  n = len(y)
  c = [[0 for _ in range(n+1)] for _ in range(m+1)]
  b = [['0' for _ in range(n+1)] for _ in range(m+1)]
  for i in range(1, m+1):
    for j in range(1, n+1):
      # 如果相等，这里的值等于斜上方的值+1
      if x[i-1] == y[j-1]:
        c[i][j] = c[i-1][j-1] + 1
        b[i][j] = 'S'
      elif c[i-1][j] >= c[i][j-1]:
        c[i][j] = c[i-1][j]
        b[i][j] = 'U'
      # 如果Left>up，left
      else:
        c[i][j] = c[i][j-1]
        b[i][j] = 'L'
  return c[m][n], b
lcs_len, b = lcs('ABCBDAB', 'BDCABA')
for _ in b:
  print(_)

def lcs_trackback(x, y):
  lcs_len, b = lcs(x, y)
  i = len(x)
  j = len(y)
  temp = []
  while i > 0 and j > 0:
    if b[i][j] == 'S': # 说明来源于左上方
      temp.append(x[i-1])
      i -= 1
      j -= 1
    elif b[i][j] == 'U': # 说明来自上方
      i -= 1
    else: # 来自左边
      j -= 1
  return lcs_len, ''.join(reversed(temp))


print(lcs_trackback('ABCBDAB', 'BDCABA'))
