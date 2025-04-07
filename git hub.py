num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

for i in range(4):
    num1 = num1 + 3

for i in range(3):
    num2 = num2 * 3
nombre1 = input("¿Cómo deseas llamar al primer número modificado?: ")
nombre2 = input("¿Cómo deseas llamar al segundo número modificado?: ")
print("El valor de %s es: %d" % (nombre1, num1))
print("El valor de {} es: {}".format(nombre2, num2))
print(f"El número llamado {nombre1} vale {num1} y el número llamado {nombre2} vale {num2}")
