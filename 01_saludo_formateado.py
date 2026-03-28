nombre=input("Ingrese su nombre: ")
while True:
    try:
        edad=int(input("Ingrese su edad: "))
        if edad<0:
            print("Ingrese una edad válida.")
            continue
        break
    except ValueError:
        print("Ingrese una edad válida.")
ciudad=input("Ingrese la ciudad donde vive: ")
print(f"Hola {nombre}. Tienes {edad} años y vives en {ciudad}.")