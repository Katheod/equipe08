import PointsFixes as pf

mu = 3.44
g_mu = lambda x: -(pow(mu, 3)*pow(x, 4)) + 2*pow(mu, 3)*pow(x, 3) - pow(mu, 2)*(mu + 1)*pow(x, 2) + pow(mu, 2)*x

print(pf.pointsFixes(g_mu, 0.7, 1000, 1e-10))