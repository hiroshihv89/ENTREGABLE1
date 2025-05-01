import numpy as np

def validar_entrada(mensaje, tipo=int, condicion=lambda x: True):
    while True:
        try:
            valor = tipo(input(mensaje))
            if condicion(valor):
                return valor
            else:
                print("El valor ingresado no cumple con la condición requerida.")
        except:
            print("Entrada no válida. Intente nuevamente.")

def ingresar_vector(nombre):
    while True:
        entrada = input(f"Ingrese los elementos del vector {nombre} separados por espacios: ").strip()
        if entrada:
            try:
                vector = np.array([float(x) for x in entrada.split()])
                return vector
            except ValueError:
                print("Asegúrate de ingresar solo números.")
        else:
            print("No se permite entrada vacía.")

# Propiedades aritméticas
def propiedad_conmutativa(A, B):
    print("\nConmutativa:")
    print("A + B =", A + B)
    print("B + A =", B + A)
    print("¿A + B == B + A?", np.allclose(A + B, B + A))

def propiedad_asociativa(A, B, C):
    print("\nAsociativa:")
    print("(A + B) + C =", (A + B) + C)
    print("A + (B + C) =", A + (B + C))
    print("¿(A + B) + C == A + (B + C)?", np.allclose((A + B) + C, A + (B + C)))

def propiedad_distributiva(A, B, escalar):
    print("\nDistributiva:")
    print(f"{escalar} * (A + B) =", escalar * (A + B))
    print(f"{escalar} * A + {escalar} * B =", escalar * A + escalar * B)
    print(f"¿{escalar}*(A+B) == {escalar}*A + {escalar}*B?", np.allclose(escalar * (A + B), escalar * A + escalar * B))

def propiedad_inverso(A):
    print("\nInverso Aditivo:")
    print("A =", A)
    print("-A =", -A)
    print("A + (-A) =", A + (-A))
    print("¿A + (-A) == 0?", np.allclose(A + (-A), np.zeros_like(A)))

def propiedad_identidad(A):
    print("\nIdentidad Aditiva:")
    identidad = np.zeros_like(A)
    print("A =", A)
    print("0 =", identidad)
    print("A + 0 =", A + identidad)
    print("¿A + 0 == A?", np.allclose(A + identidad, A))

# Menú principal
def menu_operaciones():
    print("\nPropiedades disponibles:")
    print("1. Conmutativa (A + B = B + A)")
    print("2. Asociativa ((A + B) + C = A + (B + C))")
    print("3. Distributiva (k*(A + B) = k*A + k*B)")
    print("4. Inverso aditivo (A + (-A) = 0)")
    print("5. Identidad aditiva (A + 0 = A)")

def main():
    print("Bienvenido al programa de propiedades aritméticas con NumPy")
    continuar = True
    while continuar:
        menu_operaciones()
        opcion = validar_entrada("Seleccione la propiedad que desea verificar (1-5): ", int, lambda x: 1 <= x <= 5)

        if opcion == 1:
            A = ingresar_vector("A")
            B = ingresar_vector("B")
            if A.shape != B.shape:
                print("Error: Los vectores deben tener la misma dimensión.")
            else:
                propiedad_conmutativa(A, B)

        elif opcion == 2:
            A = ingresar_vector("A")
            B = ingresar_vector("B")
            C = ingresar_vector("C")
            if A.shape != B.shape or A.shape != C.shape:
                print("Error: Todos los vectores deben tener la misma dimensión.")
            else:
                propiedad_asociativa(A, B, C)

        elif opcion == 3:
            A = ingresar_vector("A")
            B = ingresar_vector("B")
            if A.shape != B.shape:
                print("Error: Los vectores deben tener la misma dimensión.")
            else:
                escalar = validar_entrada("Ingrese un valor escalar: ", float)
                propiedad_distributiva(A, B, escalar)

        elif opcion == 4:
            A = ingresar_vector("A")
            propiedad_inverso(A)

        elif opcion == 5:
            A = ingresar_vector("A")
            propiedad_identidad(A)

        # Preguntar si desea continuar
        respuesta = input("\n¿Desea realizar otra operación? (si/no): ").strip().lower()
        if respuesta != "si":
            continuar = False
            print("Gracias por usar el programa. ¡Hasta pronto!")

if __name__ == "__main__":
    main()