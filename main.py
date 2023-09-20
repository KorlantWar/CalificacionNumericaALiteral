from clase import Calificacion

def main():
    try:
        calificacion_numerica = float(input("Ingrese la calificación numérica: "))
        calif = Calificacion(calificacion_numerica)
        calificacion_literal = calif.obtener_calificacion_literal()

        print(f"Calificación numérica: {calificacion_numerica}")
        print(f"Calificación literal: {calificacion_literal}")
    except ValueError:
        print("Por favor, ingrese una calificación numérica válida.")


if __name__ == "__main__":
    main()
