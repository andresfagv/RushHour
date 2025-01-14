class Board:
    def __init__(self, size=6):
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]

    def place_car(self, car):
        x, y = car.position
        for i in range(car.length):
            if car.type == "horizontal":
                self.grid[y][x + i] = car.id  # x representa columnas, y representa filas
            elif car.type == "vertical":
                self.grid[y + i][x] = car.id  # x representa columnas, y representa filas

    def car_can_move(self, car, direction):
        x, y = car.position
        if car.type == "horizontal":
            if direction == 'left':
                if x - 1 < 0 or self.grid[y][x - 1] != 0:
                    return False
            elif direction == 'right':
                if x + car.length >= self.size or self.grid[y][x + car.length] != 0:
                    return False
        elif car.type == "vertical":
            if direction == 'up':
                if y + car.length >= self.size or self.grid[y + car.length][x] != 0:
                    return False
            elif direction == 'down':
                if y - 1 < 0 or self.grid[y - 1][x] != 0:
                    return False
        return True

    def move_car(self, car, direction):
        if not self.car_can_move(car, direction):
            print(f"El coche {car.id} no puede moverse hacia {direction}.")
            return False

        # Elimina la posición actual del coche en la grid
        x, y = car.position
        for i in range(car.length):
            if car.type == "horizontal":
                self.grid[y][x + i] = 0
            elif car.type == "vertical":
                self.grid[y + i][x] = 0

        # Actualiza la posición del coche
        if car.type == "horizontal":
            if direction == "left":
                car.position = (x - 1, y)
            elif direction == "right":
                car.position = (x + 1, y)
        elif car.type == "vertical":
            if direction == "up":
                car.position = (x, y + 1)
            elif direction == "down":
                car.position = (x, y - 1)

        # Coloca el coche en su nueva posición en la grid
        self.place_car(car)
        return True

    def print_board(self):
        # Imprimir el tablero desde la fila superior a la inferior
        for row in self.grid:
            print(row)


class Car:
    def __init__(self, id, type, position, length):
        self.id = id
        self.type = type
        self.position = position  # (x, y)
        self.length = length


# Prueba del sistema
board1 = Board()
car1 = Car(1, "horizontal", (0, 0), 2)  # Coche en la esquina superior izquierda
car2 = Car(2, "vertical", (1, 1), 3)  # Coche en la columna 1, fila 1
board1.place_car(car1)
board1.place_car(car2)
board1.print_board()
print("")
board1.move_car(car1, "right")
board1.print_board()
print("")

