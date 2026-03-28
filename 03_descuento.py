while True:
    try:
        subtotal=float(input("Ingrese su subtotal: "))
        if subtotal<=0:
            print("Ingrese un subtotal válido.")
            continue
        break
    except ValueError:
        print("Ingrese un subtotal válido.")
print("¿Qué tipo de ciente es?\nSi es VIP, ingrese 1.\nSi es regular, ingrese 2")
tipo_cliente=input("¿Vip o regular? ")
if tipo_cliente=="vip":
    descuento=subtotal*0.15
elif tipo_cliente=="regular" and subtotal>=100:
    descuento=subtotal*0.05
else:
    descuento=0
total=subtotal-descuento
print(f"Subtotal: ${subtotal:.2f}")
print(f"Descuento aplicado: ${descuento:.2f}")
print(f"Total a pagar: ${total:.2f}")