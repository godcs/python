# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def inorderTraversal(self, root):
#         if not  root:
#             return  []
#         stack = []
#         result = []
#         cur = root
#         while stack or cur:
#             if cur:
#                 stack.append(cur)
#                 cur = cur.left
#             else:
#                 cur = stack.pop()
#                 result.append(cur.val)
#                 cur = cur.right
#         return result
import collections
from collections import deque
#
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution(object):
#     def countNodes(self, root):
#         if not root
#             return  []
#         count = 1
#         left = root.left
#         right = root.right
#         while left and right:
#             left = left.left
#             right = right.right
#         if not left and not right:
#             return 2**count-1
#         return  1+self.countNodes(root.left)+self.countNodes(root.right)
#


import csv
class Item:
    pay_rate=0.8
    all=[]
    def __init__(self,name:str,price:float,quantity=0):
        assert price>=0 ,f"price{price}is not greater than zero"
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calaulate_total_price(self,x,y):
        return x*y
    def apply_discount(self):
        self.price=self.price*self.pay_rate
    def __repr__(self):
        return f"Ttem('{self.price}',{self.quantity})"






    @staticmethod
    def is_nteger(num):
         if isinstance(num,float):
            return num.is_integer()
         elif isinstance(num, int):
            return True
         else:
             return False






item1=Item("phone",2000,5)
item1.pay_rate=0.7
item1.apply_discount()
print(Item.__repr__(item1))

my_string = 'what, am, i ,doing'
w = ''.join(my_string)

print(w)
q = my_string.split("  ")
print(q)

my_list =['a']*6
my_string=''.join(my_list)
print(my_list)
print(my_string)

from collections import defaultdict
d = defaultdict(list)
d['a']=1
d['b']=2
print(d['c'])

from itertools import product
a=[1,2]
b=[3,4]
prod = product(a,b)
print(list(prod))


