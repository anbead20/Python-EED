"""
Crea una clase que represente una estructura de datos tipo pila (stack) y otra tipo cola (queue).

La pila y la cola permitirán estas operaciones:

Crear la pila o la cola con o sin valores iniciales o a partir de otra cola o pila.

Obtener el número de elementos almacenados (tamaño).
Saber si la pila o la cola está vacía.

Vaciar completamente la pila o la cola.

Para el caso de la pila:
    - Apilar (push): se añade un elemento a la pila. Se añade al principio de esta.
    - Desapilar (pop): se saca (debe devolverse) un elemento de la pila y se elimina.
    - Leer el elemento superior de la pila sin retirarlo (top).

Para el caso de la cola:
    - Encolar (enqueue): se añade un elemento a la cola. Se añade al final de esta.
    - Desencolar (dequeue): se saca (debe devolverse) y se elimina el elemento frontal de la cola, es decir, el primer
    elemento que entró.
    - Leer el elemento frontal de la cola, es decir, el primer elemento que entró, sin retirarlo (front).

Autor: Adrián Anta Bellido
"""

from typeguard import typechecked

@typechecked
class Stack:
    def __init__(self, values=None):
        if isinstance(values, Stack):
            self.__stack = values.__stack[:]
        elif isinstance(values, list):
            self.__stack = values[:]
        else:
            self.__stack = []

    @property
    def get_stack(self):
        return self.__stack[:]

    def size(self):
        return len(self.__stack)

    def is_empty(self):
        return len(self.__stack) == 0

    def clear(self):
        self.__stack.clear()

    def push(self, value):
        self.__stack.insert(0, value)
        return f"Elemento {value} añadido a la pila."

    def pop(self):
        if self.is_empty():
            return "La pila está vacía"
        removed = self.__stack.pop(0)
        return f"Elemento {removed} eliminado de la pila."

    def top(self):
        if self.is_empty():
            return "La pila está vacía"
        return self.__stack[0]


class Queue:
    def __init__(self, values=None):
        if isinstance(values, Queue):
            self.__queue = values.__queue[:]
        elif isinstance(values, list):
            self.__queue = values[:]
        else:
            self.__queue = []


    @property
    def get_queue(self):
        return self.__queue[:]

    def size(self):
        return len(self.__queue)

    def is_empty(self):
        return len(self.__queue) == 0

    def clear(self):
        self.__queue.clear()

    def enqueue(self, value):
        self.__queue.append(value)
        return f"Elemento {value} añadido a la cola."

    def dequeue(self):
        if self.is_empty():
            return "La cola está vacía"
        removed = self.__queue.pop(0)
        return f"Elemento {removed} eliminado de la cola."

    def front(self):
        if self.is_empty():
            return "La cola está vacía"
        return self.__queue[0]

