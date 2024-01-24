precio = int(input("Pon precio en €\n"))
iva = 0
while iva not in [4, 10, 20]:
    iva = int(input('Selecciona IVA a aplicar:\n¿Quieres aplicar el 4%, 10% o el 21%?\n'))
    if iva == 4:
        if iva == 4:
            ivaAplicar = iva / 100
            resultado = precio + (precio * ivaAplicar)
        print(f"Precio introducido: {precio}€")
        print(f"IVA a aplicar: {iva}%")
        print(f"Precio con IVA: {resultado}€")