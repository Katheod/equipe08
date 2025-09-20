import numpy as np
import math as e
import matplotlib.pyplot as plt

# Question numéro 1-a
a = np.full((6,1), 1)
print("a =\n", a)

# Question numéro 1-b
b=np.arange(1, 7)
print("b = ", b)

# Question numéro 1-c
c=a.reshape(1,6)
print("c = ", c)

# Question numéro 1-d
d=c*43
print("d = ", d)

# Question numéro 1-I
I=np.identity(6)
print("I =\n", I)

# Question numéro 1-J
J=np.full((6,6),1)
print("J =\n", J)

# Question numéro 1-K
K = np.full((6,6),0)
np.fill_diagonal(K,b)
print("K = \n", K)

# Question numéro 1-L
L= 55*I -J + 2*a*c
print("L = \n", L)

# Question numéro 1-M
M=1*K ; M[:,0]=np.reshape(a,6)
print("M = \n", M)

# Question numéro 1-dd
dd=np.linalg.det(M)
print("dd = ", dd)

# Question numéro 1-x
x = np.linalg.solve(M,a)
print("x =\n", x)

# Question numéro 1-N
N = np.linalg.solve(M, np.transpose(M))
plt.matshow(N)
plt.title("Matrice N")
plt.show()
print("N =\n", N)

