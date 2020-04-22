from dossier_code.modelisation import Number


def get_primes(n):
    primes = []
    i = 1
    while len(primes)!=n: 
        a = Number(i)
        if a.is_prime():
            primes.append(i)
        i+=1
    return primes


chiffre = int(input("Entrer un nombre n entier :"))
print(get_primes(chiffre))
'''
Afficher les 5 premiers nombres premiers
a = get_primes(5) 
b = get_primes(25)
c = get_primes(1000)

print(a)
print(b)
print(c)
'''