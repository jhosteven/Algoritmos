class Calificacion:
    def __init__(self, nota):
        self.nota = nota

    def convertir_a_literal(self):
        """Convierte la calificación numérica a una calificación literal."""
        if 1 <= self.nota <= 10:
            return 'C'
        elif 11 <= self.nota <= 14:
            return 'B'
        elif 15 <= self.nota <= 17:
            return 'A'
        elif 18 <= self.nota <= 20:
            return 'AD'

    def mostrar_calificacion(self):
        literal = self.convertir_a_literal()
        print(f"La calificación numérica {self.nota} equivale a la calificación literal: {literal}")



nota = int(input("Ingrese la calificación numérica (1-20): "))



if 1 <= nota <= 20:

    calificacion = Calificacion(nota)


    calificacion.mostrar_calificacion()
else:
    print("Por favor, ingrese una calificación entre 1 y 20.")