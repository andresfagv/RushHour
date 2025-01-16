from Classes import *  # Asegúrate de que tus clases están definidas correctamente en el archivo 'Classes.py'

def main():
    # Paso 1: Crear el tablero y los coches
    board = Board()  # Usar 'board' en lugar de 'board1'

    red_car = Car(1, "horizontal", (0, 2), 2, "red")
    car2 = Car(2, "vertical", (3, 0), 3, "yellow")
    car3 = Car(3, "horizontal", (4, 4), 2, "black")
    car4 = Car(4, "vertical", (2, 3), 2, "blue")  # Nuevo coche

    # Añadir coches al tablero
    board.add_car(red_car)
    board.add_car(car2)
    board.add_car(car3)
    board.add_car(car4)

    # Paso 3: Mostrar el tablero inicial
    print("Tablero inicial:")
    board.print_board()

    # Paso 4: Simular movimientos del jugador
    while True:
        print("\nElige un coche y una dirección para moverlo:")
        print("Direcciones disponibles: 'left', 'right', 'up', 'down'")
        print("Escribe 'salir' para terminar.")

        # Entrada del jugador
        user_input = input("Formato: <id_coche> <dirección> (por ejemplo: '1 right'):\n").strip()
        if user_input.lower() == "salir":
            print("Saliendo del juego. ¡Gracias por jugar!")
            break

        try:
            # Parsear la entrada
            car_id, direction = user_input.split()
            car_id = int(car_id)

            # Seleccionar el coche desde el tablero
            car = board.get_car(car_id)  # Obtener el coche directamente desde el tablero

            if car:
                # Intentar mover el coche
                if board.move_car(car, direction):
                    print(f"Coche {car.id} movido hacia {direction}.")
                else:
                    print(f"Movimiento no válido para el coche {car.id} hacia {direction}.")
            else:
                print(f"No se encontró un coche con ID {car_id}.")

            # Mostrar el tablero actualizado
            board.print_board()

            # Comprobar si el coche rojo ha ganado
            if board.winner(red_car):
                print("\n¡El coche rojo ha salido del tablero! ¡Has ganado!")
                break

        except Exception as e:
            print(f"Entrada inválida: {e}. Por favor, inténtalo de nuevo.")

if __name__ == "__main__":
    main()
