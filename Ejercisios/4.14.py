import math


class CalculadoraRaizCuadrada:
    def __init__(self, numero):
        self.numero = numero

    def calcular_raiz_cuadrada(self):
        """Calcula la raíz cuadrada del número."""
        if self.numero < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
        return math.sqrt(self.numero)

    def mostrar_raiz_cuadrada(self):
        raiz_cuadrada = self.calcular_raiz_cuadrada()
        print(f"La raíz cuadrada de {self.numero} es {raiz_cuadrada:.4f}")



numero = float(input("Ingrese un número: "))


calculadora = CalculadoraRaizCuadrada(numero)


calculadora.mostrar_raiz_cuadrada()
