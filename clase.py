class Calificacion:
    def __init__(self, calificacion_numerica):
        self.calificacion_numerica = calificacion_numerica

    def obtener_calificacion_literal(self):
        if self.calificacion_numerica >= 9.1:
            return "A Excelente"
        elif self.calificacion_numerica >= 8.1:
            return "B Muy bien"
        elif self.calificacion_numerica >= 7.5:
            return "C Bien"
        else:
            return "R Reprobado"