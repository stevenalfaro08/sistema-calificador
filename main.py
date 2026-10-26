# Curso: Fundamentos de Tecnologia Digitales
# Profesor: Adonis Aleman G.
# Estudiante: Steven Alfaro Rodriguez. C6C234

def solicitar_nota(numero):
    """Solicita una nota entre 0 y 100 y  que valide la entrada."""
    while True:
        try:
            nota = float(input(f"Ingrese la nota {numero} (0 a 100): "))
            if 0 <= nota <= 100:
                return nota
            print("La nota debe estar entre 0 y 100.")
        except ValueError:
            print("Entrada no valida. Ingrese un numero.")


def calcular_promedio(notas):
    """Devuelve el promedio de una lista de notas."""
    return sum(notas) / len(notas)


def main():
    print("=== Sistema de registro de calificaciones ===")
    nombre = input("Ingrese el nombre del estudiante: ").strip()

    while not nombre:
        print("El nombre no puede quedar vacio.")
        nombre = input("Ingrese el nombre del estudiante: ").strip()

    cantidad = 3
    notas = []

    for numero in range(1, cantidad + 1):
        notas.append(solicitar_nota(numero))

    promedio = calcular_promedio(notas)

    print("\n=== Resultado ===")
    print(f"Estudiante: {nombre}")
    print("Notas:", ", ".join(f"{nota:.2f}" for nota in notas))
    print(f"Promedio: {promedio:.2f}")

    if promedio >= 70:
        print("Estado: Aprobado")
    else:
        print("Estado: Reprobado")


if __name__ == "__main__":
    main()
