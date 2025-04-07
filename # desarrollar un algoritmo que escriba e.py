# desarrollar un algoritmo que escriba en pantalla uno despues del otro, los resultados de la funcion n^x desde 0 hasta hasta n, con n entero maximo 9 y x entero maximo 9.

n=int(input("ingrese un numero entero entre 0 y 9: "))
x=int(input("ingrese un numero entero entre 0 y 9: "))
if 0<=n<=9 and 0<=x<=9:
    for i in range(x+1):
        z=print(f"{n}^{i}={n**i}")
else:
    print("los numeros no son validos")
print(f"el resultado es {z}")
print("fin del programa")