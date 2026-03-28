while True:
    try:
        distancia=float(input("Ingrese la distancia recorrida en km: "))
        if distancia<=0:
            print("La distancia debe ser positiva.")
            continue
        break
    except ValueError:
        print("Ingrese una distancia válida.")
while True:
    try:
        hora=int(input("Ingrese la hora del viaje. Debe ser una hora entera (0-23): "))
        if hora<0 or hora>23:
            print("Ingrese una hora válida.")
            continue
        break
    except ValueError:
        print("Ingrese una hora válida.")
tarifa_base=1
if hora >=6 and hora<=19:
    horario="diurno"
    costo_km=0.5
else:
    horario="nocturno"
    costo_km=0.65
recargo=2 if distancia>10 else 0
total=tarifa_base+(distancia*costo_km)+recargo
print(f"Horario: {horario}")
print(f"Distancia: {distancia} km")
print(f"Total a pagar: ${total:.2f}")