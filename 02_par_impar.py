while True:
    try:
        numero=int(input("Ingrese un número entero: "))
        break
    except ValueError:
        print("Su número no es válido.")

if numero%2==0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

while True:
    try:
        edad=int(input("Ingrese su edad: "))
        if edad<0:
            print("Ingrese una edad válida")
            continue
        break
    except ValueError:
        print("Lo que usted ingresó no es válido.")
if edad>=18:
    print("Usted es mayor de edad.")
else:
    print("Usted es menor de edad.")