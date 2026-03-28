while True:
    try:
        n1=float(input("Ingrese la primera nota: "))
        if n1<0 or n1>100:
            print("Error: nota inválida.")
            continue
        break
    except ValueError:
        print("Error: nota inválida.")
while True:
    try:
        n2=float(input("Ingrese la segunda nota: "))
        if n2<0 or n2>100:
            print("Error: nota inválida.")
            continue
        break
    except ValueError:
        print("Error: nota inválida.")
while True:
    try:
        n3=float(input("Ingrese la tercera nota: "))
        if n3<0 or n3>100:
            print("Error: nota inválida.")
            continue
        break
    except ValueError:
        print("Error: nota inválida.")
promedio=(n1+n2+n3)/3
def clasificar(nota):
    if nota>=90:
        return"Excelente"
    elif nota>=80:
        return"Muy bueno"
    elif nota>=70:
        return"Bueno"
    elif nota>=60:
        return"Supletorio"
    else:
        return"Reprobado"
print(f"Promedio: {promedio:.2f}")
print(f"Nota 1: {n1} -> {clasificar(n1)}")
print(f"Nota 2: {n2} -> {clasificar(n2)}")
print(f"Nota 3: {n3} -> {clasificar(n3)}")