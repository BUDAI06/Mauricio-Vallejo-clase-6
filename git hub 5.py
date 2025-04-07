n = int(input("Escribe un número entre 0 y 20: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("El factorial de", n, "es:", factorial)
