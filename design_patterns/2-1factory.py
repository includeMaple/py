# from abc import ABCMeta, abstractmethod

# # 抽象产品类product，实际是接口，用来约束具体产品的方法，以及方法需要传递的参数
# class Payment(metaclass=ABCMeta):
#   @abstractmethod # 约束这个类必须有pay方法
#   def pay(self, money):
#     pass

# # 具体产品类concrete product
# class Alipay(Payment): # 这里没有复写
#   def pay(self, money):
#     print('用支付宝支付了%s元' % money)

# # 具体产品类concrete product
# class WechatPay(Payment):
#   def pay(self, money): # 覆写了pay方法
#     print('用微信支付了%s元' % money)

# # creator 工厂角色，用来创建具体产品
# class PaymentFactory:
#   def create_payment(self, method):
#     if method == 'alipay':
#       return Alipay()
#     if method == 'wechat':
#       return WechatPay()
#     else:
#       raise TypeError("No such payment named %s" % method)

# pay = PaymentFactory()
# p = pay.create_payment('alipay')
# p.pay(100)

#********************** 添加花呗支付
from abc import ABCMeta, abstractmethod

# 抽象产品类product，实际是接口，用来约束具体产品的方法，以及方法需要传递的参数
class Payment(metaclass=ABCMeta):
  @abstractmethod # 约束这个类必须有pay方法
  def pay(self, money):
    pass

# 具体产品类concrete product
class Alipay(Payment): # 这里没有复写
  def __init__(self, isHuabei=False):
    self.isHuabei = isHuabei
  def pay(self, money):
    if self.isHuabei:
      print('用花呗支付了%s元' % money)
    else:
      print('用支付宝支付了%s元' % money)

# 具体产品类concrete product
class WechatPay(Payment):
  def pay(self, money): # 覆写了pay方法
    print('用微信支付了%s元' % money)

# creator 工厂角色，用来创建具体产品
class PaymentFactory:
  def create_payment(self, method):
    if method == 'alipay':
      return Alipay()
    elif method == 'huabei':
      return Alipay(isHuabei=True)
    elif method == 'wechat':
      return WechatPay()
    else:
      raise TypeError("No such payment named %s" % method)

pay = PaymentFactory()
p = pay.create_payment('huabei')
p.pay(100)