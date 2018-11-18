import numpy as np
from numpy import dot
from numpy import mat
from numpy.linalg import inv

#a = np.arange(15).reshape(3,5)
#print(a.shape)

A = np.mat([[1,2]])

print('A:\n' ,A)

print('A.T:\n',A.T)

B = mat([[1,2],[2,3],[3,4],[4,5]])

print('B:\n',B)
print('------------------')
print(B[0,:])
print('-------------------')
print(B[:,1])





