from numpy import linalg
import numpy as np

print('Task 1(A-B):\n',)

a = np-matrix([[1,2],[4,1]])
b = np.matrix([[2,-3],[-4,1]])
sol = (a*b)-(b*a)
print('Answer 1:\n', sol)

print('Task 2(A^2)(\n')
c = np.matrix([[-1,2],[0,1]])
print('Answer 2:\n',c**2)

print('Task 3 (A^2)\n')
d = np.matrix([[3,5],[6,-1]])
i = np.matrix([[6,1],[-3,2]])
print ('Answer 3:\n',d*i)

print('Task 4\n')
f = np.linalg.det([[2,3,4],[1,0,6],[7,8,9]])
print('Answer 4:\n',f)

print('Task 5\n')
e = np.linalg.det([[1,2,3,4],[-2,1,-4,3],[3.-4.-1,2],[4,3,-2,-1]])
print('Answer 5:\n',e)

print('Task 6\n')
j = np.linalg-inv([[1,2,-3],[0.1,2],[0,0,1]])
print('Answer 6:\n',j)

print("Task 7\n")
k = np.linalg.matrix_rank([[1,2,3,4],[3,-1,2,5],[1.2,3,4],[1,3,4,5]])
print('Answer 7:\n',k)

print('Task 8, method kramer',)
del0 = np.linalg.det([[14,4,6],[5,-3,2],[10,-11,5]])
del1 = np.linalg.det([[30,4,6],[15,-3,2],[36,-11,5]])
del2 = np.linalg.det([[14,30,6],[5,15,2],[10,36,5]])
del3 = np.linalg.det([[14,4,30],[5,-3,15],[10,-11,36]])


x1 = del1/del0
x2 = del2/del0
x3 = del3/del0
 
print("x=",x1,"y=",y1,"z=",z1)
