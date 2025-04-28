"""
Implementa la clase BankAccount. Cada cuenta corriente tiene un número de cuenta de 10 dígitos. El número
de cuenta se genera de forma aleatoria cuando se crea una cuenta nueva y no puede haber dos objetos con el mismo
número de cuenta. La cuenta se puede crear con un saldo inicial; en caso de no especificar saldo, se pondrá a cero
inicialmente. En una cuenta se pueden hacer ingresos y gastos. También es posible hacer una transferencia entre una
cuenta y otra. No se permite el saldo negativo. En el siguiente capítulo se propone un ejercicio como mejora de este,
en el que se pide llevar un registro de los movimientos realizados.

Programa principal:

cuenta1 = BankAccount()
cuenta2 = BankAccount(1500)
cuenta3 = BankAccount(6000)
print(cuenta1)
print(cuenta2)
print(cuenta3)
cuenta1.deposit(2000)
cuenta2.withdraw(600)
cuenta3.deposit(75)
cuenta1.withdraw(55)
cuenta2.transfer(cuenta3, 100)
print(cuenta1)
print(cuenta2)
print(cuenta3)
Salida

Número de cta: 6942541557 Saldo: 0,00 €
Número de cta: 9319536518 Saldo: 1500,00 €
Número de cta: 7396941518 Saldo: 6000,00 €
Número de cta: 6942541557 Saldo: 1945,00 €
Número de cta: 9319536518 Saldo: 800,00 €
Número de cta: 7396941518 Saldo: 6175,00 €

Autor: Adrián Anta Bellido
"""
from __future__ import annotations
import random

def generate_account_number():
    while True:
        number = f"{random.randint(0, 9999999999):010}"
        if number not in BankAccount.used_accounts:
            BankAccount.used_accounts.add(number)
            return number

class BankAccount:
    used_accounts = set()

    def __init__(self, money: float = 0.0):
        if money < 0:
            raise ValueError("El saldo no puede ser negativo")

        self.money = money
        self.number = generate_account_number()

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Cantidad inválida")
        self.money += amount

    def withdraw(self, amount: float):
        if amount <= 0 or amount > self.money:
            raise ValueError("No se puede retirar esa cantidad")
        self.money -= amount

    def transfer(self, other: BankAccount, amount: float):
        self.withdraw(amount)
        other.deposit(amount)

    def __str__(self):
        return f"Número de cta: {self.number} Saldo: {self.money:.2f} €"


if __name__ == "__main__":
    cuenta1 = BankAccount()
    cuenta2 = BankAccount(1500)
    cuenta3 = BankAccount(6000)

    print(cuenta1)
    print(cuenta2)
    print(cuenta3)

    cuenta1.deposit(2000)
    cuenta2.withdraw(600)
    cuenta3.deposit(75)
    cuenta1.withdraw(55)
    cuenta2.transfer(cuenta3, 100)

    print(cuenta1)
    print(cuenta2)
    print(cuenta3)

