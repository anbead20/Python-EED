from __future__ import annotations
from typeguard import typechecked

@typechecked
class Vehicle:
    vehicles_created = 0  # Atributo de clase para contar vehículos creados
    total_kilometers = 0  # Atributo de clase para el kilometraje total

    def __init__(self):
        self.__kilometers_traveled = 0  # Atributo de instancia para el kilometraje de cada vehículo
        Vehicle.vehicles_created += 1

    @property
    def kilometers_traveled(self):
        return self.__kilometers_traveled

    @classmethod
    def get_total_kilometers(cls):
        return cls.total_kilometers

    def travel(self, kilometers: int):
        """Método para viajar, incrementa los kilómetros recorridos"""
        if kilometers < 0:
            raise ValueError("Los kilómetros no pueden ser negativos.")
        self.__kilometers_traveled += kilometers
        Vehicle.total_kilometers += kilometers

    def __str__(self):
        return f"Kilómetros recorridos: {self.__kilometers_traveled} km"

@typechecked
class Bike(Vehicle):
    def __init__(self):
        super().__init__()

    def do_wheelie(self):
        """Método para hacer el caballito con la bicicleta"""
        print("¡Estás haciendo el caballito con la bicicleta!")

@typechecked
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.__fuel = 0  # Atributo de instancia para el combustible restante en el coche

    @property
    def fuel(self):
        return self.__fuel

    def burn_rubber(self):
        """Método para quemar rueda, consume 1 litro de combustible"""
        if self.__fuel >= 1:
            self.__fuel -= 1
            print("¡Quemando rueda!")
        else:
            print("No hay suficiente combustible para quemar rueda.")

    def fill_tank(self):
        """Método para llenar el depósito a 50 litros"""
        self.__fuel = 50
        print("El depósito se ha llenado a 50 litros.")

    def travel(self, kilometers: int):
        """Método para viajar, disminuye el combustible según los kilómetros recorridos"""
        fuel_needed = kilometers * 0.1
        if fuel_needed > self.__fuel:
            kilometers = self.__fuel / 0.1
            self.__fuel = 0  # Se acaba el combustible
        else:
            self.__fuel -= fuel_needed
        super().travel(kilometers)

    def __str__(self):
        return f"Nº Vehículo: Coche - Kilómetros recorridos: {self.kilometers_traveled} km - Combustible restante: {self.__fuel} litros"

def show_menu():
    print("""
    VEHÍCULOS
    =========
    1. Anda con la bicicleta.
    2. Haz el caballito con la bicicleta.
    3. Anda con el coche.
    4. Quema rueda con el coche.
    5. Llena el depósito del coche.
    6. Ver kilometraje de la bicicleta.
    7. Ver kilometraje del coche.
    8. Ver el combustible que queda en el depósito del coche.
    9. Ver kilometraje total.
    10. Salir.
    """)

def main():
    bike = Bike()
    car = Car()

    while True:
        show_menu()
        option = int(input("Elige una opción (1-10): "))

        if option == 1:
            kilometers = int(input("¿Cuántos kilómetros quieres recorrer con la bicicleta? "))
            bike.travel(kilometers)
        elif option == 2:
            bike.do_wheelie()
        elif option == 3:
            kilometers = int(input("¿Cuántos kilómetros quieres recorrer con el coche? "))
            car.travel(kilometers)
        elif option == 4:
            car.burn_rubber()
        elif option == 5:
            car.fill_tank()
        elif option == 6:
            print(f"Kilometraje de la bicicleta: {bike.kilometers_traveled} km.")
        elif option == 7:
            print(f"Kilometraje del coche: {car.kilometers_traveled} km.")
        elif option == 8:
            print(f"Combustible restante en el depósito del coche: {car.fuel} litros.")
        elif option == 9:
            print(f"Kilometraje total de todos los vehículos: {Vehicle.get_total_kilometers()} km.")
        elif option == 10:
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
