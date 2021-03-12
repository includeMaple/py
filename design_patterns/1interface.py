from abc import ABCMeta, abstractmethod

class Payment(metaclass=ABCMeta):
  @abstractmethod # 约束这个类必须有pay方法
  def pay(self, money):
    pass

class Alipay(Payment): # 这里没有复写
  def pay(self, money):
    pass

class WachatPay(Payment):
  def pay(self, money): # 覆写了pay方法
    pass


def finish_pay(p, money):
  print('pay:' + str(money))
  p.pay(100)

p = Alipay() # 后面函数调用直接报错
finish_pay(p, 100)