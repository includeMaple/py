# 每次添加日志自动添加时间戳
import time
import os

print(os.getcwd())
logfile = '{path}\log\{t}log.txt'.format(
  path=os.getcwd(),
  t=time.strftime('%Y-%m-%d',time.localtime(time.time()))
)
print(logfile)
def addlog(log=''):
  flog = open(logfile, 'a+')
  t = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
  strtime = '--------------------{tt}-------------------\n'.format(tt=t)
  flog.write(strtime)
  flog.write(str(log) + '\n')


