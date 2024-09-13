class CuentaBancaria:
    def __init__(self, saldo_inicial, tasa_interes_anual):
        self.saldo = saldo_inicial
        self.tasa_interes_anual = tasa_interes_anual

    def calcular_interes(self, anios):
        """Calcula el interés simple basado en el saldo inicial, la tasa de interés anual y el tiempo en años."""
        interes = self.saldo * (self.tasa_interes_anual / 100) * anios
        return interes

    def mostrar_interes(self, anios):
        interes = self.calcular_interes(anios)
        print(f"Interés generado en {anios} años: {interes:.2f}")
        return interes

    def saldo_total(self, anios):
        total = self.saldo + self.mostrar_interes(anios)
        print(f"Saldo total después de {anios} años: {total:.2f}")
        return total



saldo_inicial = float(input("Ingrese el saldo inicial de la cuenta: "))
tasa_interes_anual = float(input("Ingrese la tasa de interés anual (en %): "))
anios = int(input("Ingrese el número de años: "))


cuenta = CuentaBancaria(saldo_inicial, tasa_interes_anual)


cuenta.saldo_total(anios)
