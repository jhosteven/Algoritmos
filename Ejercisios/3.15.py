import math


class ConversorAngulos:
    def __init__(self, angulo, tipo):
        self.angulo = angulo
        self.tipo = tipo.lower()  

    def convertir(self):
        """Convierte el ángulo entre grados sexagesimales y radianes."""
        if self.tipo == 'grados':
            return self.angulo * (math.pi / 180)
        elif self.tipo == 'radianes':
            return self.angulo * (180 / math.pi)
        else:
            raise ValueError("El tipo debe ser 'grados' o 'radianes'")

    def mostrar_conversion(self):
        if self.tipo == 'grados':
            tipo_destino = 'radianes'
        elif self.tipo == 'radianes':
            tipo_destino = 'grados'
        else:
            raise ValueError("El tipo debe ser 'grados' o 'radianes'")

        angulo_convertido = self.convertir()
        print(f"{self.angulo} {self.tipo} equivalen a {angulo_convertido:.4f} {tipo_destino}")



angulo = float(input("Ingrese el ángulo: "))
tipo = input("Ingrese el tipo ('grados' o 'radianes'): ")


conversor = ConversorAngulos(angulo, tipo)


conversor.mostrar_conversion()
