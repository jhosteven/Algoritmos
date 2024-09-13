class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def dibujar(self):
        """Dibuja un cuadrado en la consola con el lado especificado."""
        for i in range(self.lado):
            if i == 0 or i == self.lado -1:

                print('*' * self.lado)
            else:

                print('*' + ' ' * (self.lado - 2) + '*')


lado = int(input("Ingrese la longitud del lado del cuadrado: "))


cuadrado = Cuadrado(lado)


cuadrado.dibujar()
