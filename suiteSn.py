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
    x = x0
    for _ in range(Nmax):
        x_new = g_mu(x)
        if (abs(x_new - x)/(abs(x_new)+1e-19)) < eps:
            return x_new
        x = x_new
    raise ValueError("La méthode n'a pas convergé")


def g_mu(x, mu=3.44):
    """Fonction g_μ(x) = f(x) où f est une fonction polynomiale."""
    return (-mu**3*x**4) + 2*mu**3*x**3 - mu**2*(mu + 1)*x**2 + mu**2*x

mu = 3.44
r1 = 0
r2 = (mu - 1) / mu
r3 = ((mu-1) + math.sqrt((mu+1.0)*(mu-3.0))) / (2*mu)
r4 = ((mu-1) - math.sqrt((mu+1.0)*(mu-3.0))) / (2*mu)
g = lambda x: (-mu**3*x**4) + 2*mu**3*x**3 - mu**2*(mu + 1)*x**2 + mu**2*x
#print(r1, r2, r3, r4)
x0 = round(r3, 1)
#print(x0)
pointsFixes(g_mu, 0, 1000, 1e-10)
