reservas = {}

def reservar_zapatillas():
    print("\n-- Reservar Zapatillas --")
    if len(reservas) >= 20:
        print("No hay más stock disponible para reservas.")
        return

    nombre = input("Nombre del comprador: ").strip()
    if nombre in reservas:
        print("Ya existe una reserva con ese nombre.")
        return

    codigo = input("Digite la palabra secreta para confirmar la reserva: ")
    if codigo != "EstoyEnListaDeReserva":
        print("Código secreto incorrecto. No se realizó la reserva.")
        return

    reservas[nombre] = 1
    print("Reserva realizada exitosamente para", nombre + ".")

def buscar_reserva():
    print("\n-- Buscar Zapatillas Reservadas --")
    nombre = input("Nombre del comprador a buscar: ").strip()
    if nombre not in reservas:
        print("No se encontró ninguna reserva con ese nombre.")
        return

    pares = reservas[nombre]
    tipo = "estándar" if pares == 1 else "VIP"
    print("Reserva encontrada:", nombre, "-", pares, "par(es) (" + tipo + ").")
    
    if pares == 1:
        extra = input("¿Desea pagar adicional para VIP y reservar 2 pares? (s/n): ").lower()
        if extra == "s":
            reservas[nombre] = 2
            print("Reserva actualizada a VIP. Ahora", nombre, "tiene 2 pares reservados.")
        else:
            print("Manteniendo reserva actual.")

def cancelar_reserva():
    print("\n-- Cancelar Reserva --")
    nombre = input("Nombre del comprador cuya reserva desea cancelar: ").strip()
    if nombre in reservas:
        del reservas[nombre]
        print("La reserva de", nombre, "ha sido cancelada.")
    else:
        print("No se encontró ninguna reserva con ese nombre.")

def main():
    while True:
        print("\nTOTEM AUTOATENCIÓN RESERVA STRIKE")
        print("1.- Reservar zapatillas")
        print("2.- Buscar zapatillas reservadas")
        print("3.- Cancelar reserva de zapatillas")
        print("4.- Salir")

        opcion = input("Seleccione una opción (1-4): ").strip()

        if opcion == "1":
            reservar_zapatillas()
        elif opcion == "2":
            buscar_reserva()
        elif opcion == "3":
            cancelar_reserva()
        elif opcion == "4":
            print("\nPrograma terminado...")
            break
        else:
            print("\nDebe ingresar una opción válida!!")

main()
