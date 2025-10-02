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
