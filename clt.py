import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


def clt(n, N):
    """n: nombre de tirages, N: nombre de repetitions"""
    # tirage de n variables aleatoires uniformes sur [0,1]
    X = np.random.uniform(size=(n, N))
    # calcul de la moyenne de chaque repetition
    Y = np.mean(X, axis=0)
    # calcul de la moyenne des moyennes
    Z = np.mean(Y)
    # calcul de la variance des moyennes
    V = np.var(Y)
    return Z, V


def visualize_clt(n, N):
    """visualisation du theoreme central limite"""
    # moyenne des moyennes
    Z = np.zeros(N)
    # variance des moyennes
    V = np.zeros(N)
    # repetition de l'experience
    for i in range(N):
        Z[i], V[i] = clt(n, 1)
    # histogramme des moyennes + densite de la loi normale
    plt.title("Distribution des moyennes")
    plt.hist(Z, bins=50, density=True)
    x = np.linspace(0, 1, 100)
    plt.plot(x, stats.norm.pdf(x, loc=0.5, scale=np.sqrt(1/(12*n))))
    plt.legend(["loi normale", "moyennes"])
    plt.show()
    # histogramme des variances
    plt.title("Histogramme des variances")
    plt.hist(V, bins=50)
    plt.show()
    # nuage de points
    plt.title("Correlation entre moyenne et variance")
    plt.scatter(Z, V)
    plt.show()