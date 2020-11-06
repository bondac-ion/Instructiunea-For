"""Utilizînd ciclul FOR elaboraţi un program care afişează toate numerele pare, pentru intervalul de la 1 la n (n-este citit de la tastatură)."""
n=int(input("dati un numar:"))
for i in range(1,n):
    if i%2==0:
        print(i)
