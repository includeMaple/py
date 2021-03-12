
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

# creator抽象工厂角色，用来约束所有concrete creator
class PaymentFactory():
  @abstractmethod
  def create_payment(self):
    pass

# 下面每个contrete product有一个concrete creator
class AlipayFactory(PaymentFactory):
  def create_payment(self):
    return Alipay()

class WechatPayFactory(PaymentFactory):
  def create_payment(self):
    return WechatPay()

class HuabeiFactory(PaymentFactory):
  def create_payment(self):
    return Alipay(isHuabei=True)

phuabei = HuabeiFactory()
p = phuabei.create_payment()
p.pay(100)
pali = AlipayFactory()
pp = pali.create_payment()
pp.pay(200)
wechat = WechatPayFactory()
ppp = wechat.create_payment()
ppp.pay(300)