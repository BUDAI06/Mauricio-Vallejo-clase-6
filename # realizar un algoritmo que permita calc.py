# realizar un algoritmo que permita calcular la multiplicacion de dos numeros con sumas.
num1=int(input("Ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
c=0
z=0
while c<num2 :
    z+=num1
    c+=1
    resultado=z
    print(resultado)
    if c==num2:
        break
print(f"el resultado de la multiplicaion es {resultado}")