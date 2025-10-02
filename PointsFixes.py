import math
import numpy as np
import matplotlib.pyplot as plt

def pointsFixes(f, x0, Nmax, eps):
    """
    Trouve un point fixe de la fonction f en utilisant la méthode des points fixes.
    
    Args:
        f (function): La fonction pour laquelle trouver un point fixe.
        x0 (float): Le point de départ pour l'itération.
        Nmax (int): Le nombre maximum d'itérations.
        eps (float): La tolérance pour la convergence.
    
    Returns:
        float: Le point fixe trouvé.
    """
    e_n = []
    x = x0
    x1 = f(x)
    for i in range(Nmax):
        e_n.append(abs(x1 - x))
        if abs(x1 - x) < eps:
            return x1, e_n
        x = x1
        x1 = f(x)
    raise ValueError("La méthode n'a pas convergé")



mu = 3.44
r1 = 0
r2 = (mu - 1) / mu
r3 = ((mu-1) + math.sqrt((mu+1.0)*(mu-3.0))) / (2*mu)
r4 = ((mu-1) - math.sqrt((mu+1.0)*(mu-3.0))) / (2*mu)
print(r3, r4)

f = lambda x : -(pow(mu, 3)*pow(x, 4)) + 2*pow(mu, 3)*pow(x, 3) - pow(mu, 2)*(mu + 1)*pow(x, 2) + pow(mu, 2)*x

r, e_n = pointsFixes(f, 0.7, 1000, 1e-10)

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
