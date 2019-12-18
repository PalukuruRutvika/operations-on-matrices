import numpy as np
a=np.array(input("enter 3X3 matrix:"));
b=np.array(input("enter 3X3 matrix:"));
print a
print b
add=np.add(a,b)
print 'addition of matrices is:\n',add
sub=np.subtract(a,b)
print 'subtraction of matrices is:\n',sub
mul=np.multiply(a,b)
print 'multiplication of matrices is:\n',mul
div=np.divide(a,b)
print 'division of matrices is:\n',div
dot=np.dot(a,b)
print 'dot product of matrices is:\n',dot
square=np.sqrt(b)
print 'square root of matrix is:\n',square
trace=np.trace(a)
print 'trace of matrix is:\n',trace
rank=np.linalg.matrix_rank(a)
print 'rank of matrix is:\n',rank
inverse=np.linalg.inv(b)
print 'inverse of matrix is:\n',inverse
power=np.power(a,b)
print 'power of matrices is:\n',power
p=np.linalg.matrix_power(a,3)
print 'the power of the enterd matrix raised to 3 is\n',p
det=np.linalg.det(a)
print 'determinant of matrix is:\n',det
eigen=np.linalg.eig(a)
print'eigenvectors of matrix is:\n',eigen
solve=np.linalg.solve(a,b)#solving a linear matrix equation
print 'solving equations is:\n',solve
norm=np.linalg.norm(a)
print 'norm of matrix is:\n',norm




