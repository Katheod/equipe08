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
    x_n = x0
    x_plus_1 = f(x_n)
    for _ in range(Nmax):
        if (abs(x_plus_1 - x_n))/(abs(x_plus_1)+1e-19) < eps:
            return x_plus_1
        x_n = x_plus_1
        x_plus_1 = f(x_n)
    raise ValueError("La méthode n'a pas convergé")



mu = 3.44
r1 = 0
r2 = (mu - 1) / mu
r3 = ((mu-1) + math.sqrt((mu+1.0)*(mu-3.0))) / (2*mu)
r4 = ((mu-1) - math.sqrt((mu+1.0)*(mu-3.0))) / (2*mu)


f = lambda x : -((3.44)**3*x**4) + 2*(3.44)**3*x**3 - (3.44)**2*((3.44) + 1)*x**2 + (3.44)**2*x

pointsFixes(f, 0.5, 1000, 1e-10)



"""
# Définir la dérivée de f pour vérifier la condition de contraction
df = lambda x: -4*(3.44)**3*x**3 + 6*(3.44)**3*x**2 - 2*(3.44)**2*((3.44) + 1)*x + (3.44)**2

# Vérifier si |f'(r3)| < 1
print(f"Valeur absolue de f'(r3): {abs(df(r3))}")
if abs(df(r3)) >= 1:
    print("Attention : La méthode des points fixes peut ne pas converger car f n'est pas contractante en r3.")

# Tracer la fonction f pour visualiser les points fixes
x_vals = np.linspace(-1, 1, 500)
y_vals = [f(x) for x in x_vals]

plt.plot(x_vals, y_vals, label="f(x)")
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.scatter([r1, r2, r3, r4], [0, 0, 0, 0], color='red', label="Points fixes théoriques")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.title("Visualisation de la fonction f et des points fixes")
plt.show()

# Vérifier la contraction dans un voisinage de r3
x_test_vals = np.linspace(r3 - 0.1, r3 + 0.1, 100)
df_vals = [abs(df(x)) for x in x_test_vals]

plt.plot(x_test_vals, df_vals, label="|f'(x)|")
plt.axhline(1, color='red', linestyle='--', label="|f'(x)| = 1")
plt.scatter([r3], [abs(df(r3))], color='green', label="|f'(r3)|")
plt.xlabel("x")
plt.ylabel("|f'(x)|")
plt.legend()
plt.title("Analyse de la contraction autour de r3")
plt.show()

# Suggérer un x0 basé sur l'analyse
for x, df_val in zip(x_test_vals, df_vals):
    if df_val < 1:
        print(f"x0 suggéré : {x}")
        break
"""