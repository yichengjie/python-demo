import logging
from array import array

logging.debug('Debugging information')
a = array('H', [4000, 10, 700, 22222])
print("sum(a) is : ", sum(a))

print("a is : ", a)
t1 = a[1:3]
print("t1 : ", t1)

L = ['Google', 'Runoob', 'Taobao']
t2 = L[1:]
print("t2 : ", t2)
