from ej5 import Stack, Queue

print("Prueba de la pila")
pila = Stack([4, 5, 6])
print(pila.push(6))
print(pila.size())
print(pila.pop())
print(pila.top())

print("\nPrueba de la cola")
cola = Queue([2, 3])
print(cola.enqueue(8))
print(cola.size())
print(cola.dequeue())
print(cola.front())
