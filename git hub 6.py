n = int(input("Escribe el número de términos (n): "))
a = float(input("Escribe el valor de a: "))

suma = 0

for i in range(1, n + 1):
    suma += (1 / a) ** i

print("El resultado de la sumatoria es:", suma)
