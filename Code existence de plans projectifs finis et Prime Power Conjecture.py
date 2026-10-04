N = 2000000

# crible pour avoir le plus petit facteur premier de chaque nombre jusqu'à N
L = list(range(N + 1))
for i in range(2, int(N**0.5) + 1):
    if L[i] == i:
        for j in range(i * i, N + 1, i):
            if L[j] == j:
                L[j] = i

existence = []
inexistence = []
indetermine = []
somme_carres = []

for n in range(2, N + 1):
    # on factorise n grace au crible
    m = n
    facteurs = {}
    while m != 1:
        p = L[m]
        compteur = 0
        while m % p == 0:
            m = m // p
            compteur = compteur + 1
        facteurs[p] = compteur

    # n est une puissance de nombre premier si un seul facteur premier
    puissance_premier = len(facteurs) == 1

    # n est somme de deux carres si tous les facteurs premiers
    # congrus a 3 mod 4 ont un exposant pair (Version généralisé du théorème des deux carrés de Fermat)
    somme2carres = True
    for p in facteurs:
        if p % 4 == 3 and facteurs[p] % 2 != 0:
            somme2carres = False

    if (n % 4 == 1 or n % 4 == 2) and somme2carres:
        somme_carres.append(n)

    if puissance_premier:
        existence.append(n)
    elif (n % 4 == 1 or n % 4 == 2) and not somme2carres:
        inexistence.append(n)
    else:
        indetermine.append(n)

print("nombre d'ordres avec existence prouvee :", len(existence))
print("nombre d'ordres avec inexistence prouvee :", len(inexistence))
print("nombre d'ordres indetermines :", len(indetermine))
print("nombre d'ordres n = 1 ou 2 mod 4 et somme de deux carres :", len(somme_carres))
