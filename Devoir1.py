from PointsFixes import pointsFixes
import matplotlib.pyplot as plt
from math import sqrt, pow


# b
mu = 3.44
r1 = 0
r2 = (mu - 1) / mu
r3 = ((mu+1) + sqrt((mu+1.0)*(mu-3.0))) / (2*mu)
r4 = ((mu+1) - sqrt((mu+1.0)*(mu-3.0))) / (2*mu)
print(r1, r2, r3, r4)
f = lambda x: -(pow(mu, 3)*pow(x, 4)) + 2*pow(mu, 3)*pow(x, 3) - pow(mu, 2)*(mu + 1)*pow(x, 2) + pow(mu, 2)*x
print(f(r1), f(r2), f(r3), f(r4))

r, e_n = pointsFixes(f, 0.8, 1000, 1e-10)
print(r, len(e_n))


plt.figure(1)
plt.semilogy(range(len(e_n)), e_n)
plt.xlabel("itérations (N)")
plt.ylabel("||E_n||")
plt.title("Figure 1")
plt.grid()
plt.show()

e_n1= e_n[1:]
e_n = e_n[:-1]

plt.figure(2)
plt.loglog(e_n, e_n1)
plt.xlabel("||E_n||")
plt.ylabel("||E_{n+1}||")
plt.title("Figure 2")
plt.grid()
plt.show()