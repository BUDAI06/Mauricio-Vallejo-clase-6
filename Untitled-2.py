n = int(input("Escribe un número: "))
suma = 0

for i in range(1, n + 1):
    if i % 2 != 0:
        suma += i

print("La suma de los números impares entre 1 y", n, "es:", suma)
print("fin de programa")