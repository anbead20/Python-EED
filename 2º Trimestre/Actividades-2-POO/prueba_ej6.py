from ej6 import Duration

# Prueba básica de la clase Duration
t1 = Duration(1, 20, 30)
t2 = Duration(2, 75, -10)
t3 = Duration(t2)

print("Duraciones creadas:")
print("t1:", t1.return_string())  # 1h 20m 30s
print("t2:", t2.return_string())  # 3h 14m 50s
print("t3:", t3.return_string())  # 3h 14m 50s

# Suma y resta de objetos
t4 = t1.add_and_subtract_objects(t2, "+")
print("t1 + t2 =", t4.return_string())  # 4h 35m 20s

t5 = t2.add_and_subtract_objects(t1, "-")
print("t2 - t1 =", t5.return_string())  # 2h -5m -40s

# Suma y resta de tiempo
t1.add_and_subtract_time(0, 40, 30)
print("t1 tras añadir 40m 30s:", t1.return_string())  # 2h 1m 0s

t2.add_and_subtract_time(-1, -15, -50)
print("t2 tras restar 1h 15m 50s:", t2.return_string())  # 2h 59m 0s

