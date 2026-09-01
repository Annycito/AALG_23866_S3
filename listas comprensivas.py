#{2*x | x e N, x <= 10}     // CONJUNTO DE LOS PRIMEROS 10 NÚMEROS PARES
a = [2*x for x in range(1,11,1)]    
print(a)

#Ejercicio 2 lista intencional para devolverme los numero multiplos de 3 a partir del 4 hasta el 20
b = [x for x in range(4,21) if x % 3 == 0]
print(b)
