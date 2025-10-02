import PointsFixes as pf
import matplotlib.pyplot as plt

mu = 3.44
g_mu = lambda x: -(pow(mu, 3)*pow(x, 4)) + 2*pow(mu, 3)*pow(x, 3) - pow(mu, 2)*(mu + 1)*pow(x, 2) + pow(mu, 2)*x

r, e_n = pf.pointsFixes(f, 0.7, 1000, 1e-10)

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