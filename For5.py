"""Utilizînd ciclul FOR elaboraţi un program care să calculeze suma numerelor de la 1 la n, 
care se împart la 3 şi 5 pentru oricare n întrodus de la tastatură."""
n=int(input("dati un numar:"))
s=0
for i in range(1,n):
    if (i%3==0) and (i%5==0):
        s+=i
print("suma este =",s)