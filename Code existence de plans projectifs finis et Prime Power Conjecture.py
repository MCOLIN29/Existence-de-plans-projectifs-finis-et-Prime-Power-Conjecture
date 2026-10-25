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

# on factorise n grace au crible
for n in range(2, N + 1):
    m = n
    facteurs = {}
    while m != 1:
        p = L[m]
        compteur = 0
        while m % p == 0:
            m = m // p
            compteur = compteur + 1
        facteurs[p] = compteur


    puissance_premier = len(facteurs) == 1 # n est une puissance de nombre premier si un seul facteur premier

    # n est somme de deux carres si tous les facteurs premiers
    # congrus a 3 mod 4 ont un exposant pair (Version généralisé du théorème des deux carrés de Fermat)
    somme2carres = True
    for p in facteurs:
        if p % 4 == 3 and facteurs[p] % 2 != 0:
            somme2carres = False
            
    # vérifie si n = 1 mod 4 ou n = 2 mod 4 et n est la somme de deux carres (cas où Bruck - Ryser échoue)
    if (n % 4 == 1 or n % 4 == 2) and somme2carres:
        somme_carres.append(n)
        
    # existence d'un plan projectif fini si n est une puissance de nombre premier 
    if puissance_premier: 
        existence.append(n)
        
    #inexistence d'un plan projectif fini si n = 1 mod 4 ou n = 2 mod 4 et n n'est pas la somme de deux carres (Bruck -Ryser) 
    elif (n % 4 == 1 or n % 4 == 2) and not somme2carres:
        inexistence.append(n)
    # dernier cas où on ne peut pas conclure
    else:
        indetermine.append(n)

print("nombre d'ordres avec existence prouvee :", len(existence))
print("nombre d'ordres avec inexistence prouvee :", len(inexistence)+2) #+2 pour l'inexstence des plans projectifs d'ordre 6 et 10
print("nombre d'ordres indetermines :", len(indetermine)-2) #-2 pour l'inexstence des plans projectifs d'ordre 6 et 10
print("En particulier, nombre d'ordres où n = 1 mod 4 ou n = 2 mod 4 et n est la somme de deux carres :", len(somme_carres))
