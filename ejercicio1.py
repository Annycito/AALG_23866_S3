lista_nombres = []
v1, v2, v3, v4 =["Agregar nombre y apellido",
                 "Listar nombres completos",
                 "Eliminar un nombre",
                 "Salir"]
while True:
    print("\n****MENÚ REPETITIVO *****")
    print(f"1) {v1}")
    print(f"2) {v2}")
    print(f"3) {v3}")
    print(f"4) {v4}")
    opcion = input("Seleccione una opción (1-4): ")
    if opcion == "1":
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        nombre_completo = f"{nombre} {apellido}"
        lista_nombres.append(nombre_completo)
        print(f"'{nombre_completo}' ha sido registrado en la lista.")        
    elif opcion == "2":
        if not lista_nombres:
            print("La lista está vacía actualmente.")
        else:
            print("\n****LISTA DE NOMBRES ****")
            for i, nombre in enumerate(lista_nombres, 1):
                print(f"{i}. {nombre}")                
    elif opcion == "3":
        buscar = input("Ingrese el nombre exacto que desea eliminar: ")
        if buscar in lista_nombres:
            lista_nombres.remove(buscar)
            print(f"'{buscar}' se eliminó correctamente.")
        else:
            print("No se encontró ninguna coincidencia en la lista.")        
    elif opcion == "4":
        print("Finalizando la aplicación... ¡Adiós!")
        break
     
    else:
        print("Entrada inválida. Por favor, marque un número del 1 al 4.")