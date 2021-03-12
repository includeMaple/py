import log
# 一共多少个盘子
disc_num = 2

def hanoi(num, a, b, c):
  if num > 0:
    # n-1个盘子from a pass c to b
    hanoi(num-1, a, c, b)
    # 第n个盘子的移动
    logStr = 'disc%s moving from %s to %s' % (str(num), a, c)
    log.addlog(logStr)
    print(logStr)
    # n-1个盘子from b pass a to c
    hanoi(num-1, b, a, c)

hanoi(disc_num, 'A', 'B', 'C')