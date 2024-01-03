# class college:
#     def __init__(self, cn):
#         self.cn = cn
#     def get_name(self):
#         return 2
#     def set_name(self, name):
#         self.__name = name
class students(college):
    def __init__(self, nam, cn):
        self.nam = nam
        super().__init__(cn)

s3 = students("vediya", "RCP")
print(s3.nam, s3.cn)
print(s3.get_name())
from abc import ABCMeta, abstractmethod
class product(metaclass=ABCMeta):
    @abstractmethod
    def return_policy(self):
        pass

class mobile(product):
    def return_policy(self):
        pass

class shoe(mobile):
    # def return_policy(self):
    #     pass
    pass

obj = mobile()

#static variable"
class mobile:
    d = 0
    def __init__(self, price):
        self.price = price
        mobile.d += 1
    def discount(self):
        self.price = self.price * (1-(mobile.d/100))
        return self.price
    def get_d():
        return mobile.d

class shoe(mobile):
    def __init__(self, price):
        self.price = price
        mobile.d += 1
obj = mobile(20000)
obj1 = mobile(20000)
obj2 = mobile(20000)
obj3 = mobile(20000)
obj5 = shoe(1000)
print(mobile.get_d())
