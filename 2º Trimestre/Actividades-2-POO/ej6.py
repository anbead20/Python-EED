"""
Crea una clase para almacenar duraciones de tiempo (Duration). Los objetos de esta clase son intervalos de tiempo
y se crean de la forma:

t1 = Duration(1, 20, 30) # almacenará 1 hora, 20 minutos y 30 segundos.

t2 = Duration(2, 75, -10) # almacenará 3 horas, 14 minutos y 50 segundos.

t3 = Duration(t2) # almacenará las horas, minutos y segundos del objeto t2

Crea los getters y setters mediante propiedades y métodos para:

Sumar y restar objetos de la clase sobrecargando operadores (el resultado es otro objeto).
Sumar y restar segundos, minutos o horas (se cambia el objeto actual).
Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea 10h 35m 5s.

Autor: Adrián Anta Bellido
"""

from typeguard import typechecked

@typechecked
class Duration:
    def __init__(self, hours, minutes=None, seconds=None):
        if isinstance(hours, Duration):
            self.__hours = hours.__hours
            self.__minutes = hours.__minutes
            self.__seconds = hours.__seconds
        else:
            self.__hours = hours
            self.__minutes = minutes
            self.__seconds = seconds

        self.__normalize_time()

    def __normalize_time(self):
        total_seconds = self.__hours * 3600 + self.__minutes * 60 + self.__seconds
        self.__hours = total_seconds // 3600
        self.__minutes = (total_seconds % 3600) // 60
        self.__seconds = total_seconds % 60

    @property
    def hours(self):
        return self.__hours

    @property
    def minutes(self):
        return self.__minutes

    @property
    def seconds(self):
        return self.__seconds

    def add_and_subtract_time(self, hours, minutes, seconds):
        self.__hours += hours
        self.__minutes += minutes
        self.__seconds += seconds
        self.__normalize_time()

    def add_and_subtract_objects(self, other, operation="+"):
        if isinstance(other, Duration):
            if operation == "+":
                return Duration(self.__hours + other.hours, self.__minutes + other.minutes,
                                self.__seconds + other.seconds)
            elif operation == "-":
                return Duration(self.__hours - other.hours, self.__minutes - other.minutes,
                                self.__seconds - other.seconds)
        return NotImplemented

    def return_string(self):
        return f"{self.__hours}h {self.__minutes}m {self.__seconds}s"


