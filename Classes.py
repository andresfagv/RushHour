class Board:
    def __init__(self, size=6):
        self.size = size
        self.grid = [[0 for _ in range(size)] for _ in range(size)]
        self.cars = {}

    def place_car(self, car):
        x, y = car.position
        for i in range(car.length):
            if car.type == "horizontal":
                self.grid[y][x + i] = car.id  # x representa columnas, y representa filas
            elif car.type == "vertical":
                self.grid[y + i][x] = car.id  # x representa columnas, y representa filas

    def add_car(self, car):
        """Añade un coche al tablero y lo posiciona."""
        self.cars[car.id] = car
        self.place_car(car)

    def get_car(self, car_id):
        return self.cars.get(car_id, None)

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
                if y - 1 < 0 or self.grid[y - 1][x] != 0:  # Espacio arriba
                    return False
            elif direction == 'down':
                if y + car.length >= self.size or self.grid[y + car.length][x] != 0:  # Espacio abajo
                    return False
        return True

    def move_car(self, car, direction):
        if not self.car_can_move(car, direction):
            print(f"El coche {car.color} no puede moverse hacia {direction}.")
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
                car.position = (x, y - 1)  # Mover hacia arriba
            elif direction == "down":
                car.position = (x, y + 1)  # Mover hacia abajo

        # Coloca el coche en su nueva posición en la grid
        self.place_car(car)
        return True

    def winner (self, car):
        if car.position == (4, 2):
            return True

    def print_board(self):
        # Imprimir el tablero desde la fila superior a la inferior
        for row in self.grid:
            print(row)


class Car:
    def __init__(self, id, type, position, length, color):
        self.id = id
        self.type = type
        self.position = position  # (x, y)
        self.length = length
        self.color = color


