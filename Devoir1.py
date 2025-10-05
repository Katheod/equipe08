from PointsFixes import pointsFixes
import matplotlib.pyplot as plt
from math import sqrt, pow
from numpy import polyfit, log
# Toutes les racines et la fonction.
"""
r1 = 0
r2 = (mu - 1) / mu
r3 = ((mu+1) + sqrt((mu+1.0)*(mu-3.0))) / (2*mu)
r4 = ((mu+1) - sqrt((mu+1.0)*(mu-3.0))) / (2*mu)
f = lambda x: -(pow(mu, 3)*pow(x, 4)) + 2*pow(mu, 3)*pow(x, 3) - pow(mu, 2)*(mu + 1)*pow(x, 2) + pow(mu, 2)*x
"""
# Question b
mu = 3.44
r3 = ((mu+1) + sqrt((mu+1.0)*(mu-3.0))) / (2*mu)
f = lambda x: -(pow(mu, 3)*pow(x, 4)) + 2*pow(mu, 3)*pow(x, 3) - pow(mu, 2)*(mu + 1)*pow(x, 2) + pow(mu, 2)*x

# Récupérer le point fixes et la liste d'erreurs.
r, e_n = pointsFixes(f, 0.8, 500, 1e-10)

#Créer la figure 1.
plt.figure(1)
plt.semilogy(range(len(e_n)), e_n)
plt.xlabel('itérations')
plt.ylabel('||E_n||')
plt.title("||E_n|| en échelle semi-logarithmique")
plt.legend()
plt.grid()

#Créer ||E_{n+1}|| et ||E_n||. 
e_n1= e_n[1:]
e_n = e_n[:-1]

#Créer la figure 2
plt.figure(2)
plt.loglog(e_n, e_n1, label="log(C) + p*log(||E_n||)")
plt.xlabel('||E_n||')
plt.ylabel('||E_{n+1}||')
plt.title("||E_{n+1}|| en fonction de ||E_n|| en échelle double-logarithmique")
plt.legend()
plt.grid()



# Trouver l'ordre de convergence.
log_errors_n = log(e_n)
log_errors_n1 = log(e_n1)
p, _ = polyfit(log_errors_n, log_errors_n1, 1)



# Question c
mu = 3.095
r4 = ((mu+1) - sqrt((mu+1.0)*(mu-3.0))) / (2*mu)
f = lambda x: -(pow(mu, 3)*pow(x, 4)) + 2*pow(mu, 3)*pow(x, 3) - pow(mu, 2)*(mu + 1)*pow(x, 2) + pow(mu, 2)*x

# Récupérer le point fixes et la liste d'erreurs.
r, e_n = pointsFixes(f, 0.5, 1000, 1e-10)

#Créer la figure 1.
plt.figure(3)
plt.semilogy(range(len(e_n)), e_n)
plt.xlabel('itérations')
plt.ylabel('||E_n||')
plt.title("||E_n|| en échelle semi-logarithmique")
plt.legend()
plt.grid()

#Créer ||E_{n+1}|| et ||E_n||. 
e_n1= e_n[1:]
e_n = e_n[:-1]

#Créer la figure 2
plt.figure(4)
plt.loglog(e_n, e_n1, label="log(C) + p*log(||E_n||)")
plt.xlabel('||E_n||')
plt.ylabel('||E_{n+1}||')
plt.title("||E_{n+1}|| en fonction de ||E_n|| en échelle double-logarithmique")
plt.legend()
plt.grid()
plt.show()


# Trouver l'ordre de convergence.
log_errors_n = log(e_n)
log_errors_n1 = log(e_n1)
p, _ = polyfit(log_errors_n, log_errors_n1, 1)
