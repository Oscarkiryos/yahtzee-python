"""
Yahtzee clásico para dos jugadores.
Interfaz: consola.
Versión educativa: incluye las 13 categorías, bonificación superior y
bonificaciones por Yahtzees adicionales. No implementa las reglas especiales
de comodín (Joker) de la versión oficial.
"""

import random
from collections import Counter

CATEGORIES = {
    "unos": "Unos",
    "doses": "Doses",
    "treses": "Treses",
    "cuatros": "Cuatros",
    "cincos": "Cincos",
    "seises": "Seises",
    "trio": "Trío (3 iguales)",
    "poker": "Póker (4 iguales)",
    "full": "Full house",
    "escalera_pequena": "Escalera pequeña",
    "escalera_grande": "Escalera grande",
    "yahtzee": "Yahtzee (5 iguales)",
    "azar": "Azar",
}

UPPER_CATEGORIES = ["unos", "doses", "treses", "cuatros", "cincos", "seises"]
LOWER_CATEGORIES = [
    "trio", "poker", "full", "escalera_pequena",
    "escalera_grande", "yahtzee", "azar"
]


def lanzar_dado():
    """Devuelve un entero aleatorio entre 1 y 6, ambos incluidos."""
    return random.randint(1, 6)


def lanzar_dados(cantidad=5):
    """Genera una lista con la cantidad indicada de dados."""
    return [lanzar_dado() for _ in range(cantidad)]


def es_yahtzee(dados):
    """True si los cinco dados muestran el mismo número."""
    return len(dados) == 5 and len(set(dados)) == 1


def tiene_escalera_pequena(dados):
    """True si existe una secuencia de al menos cuatro valores consecutivos."""
    valores = set(dados)
    secuencias = ({1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6})
    return any(secuencia.issubset(valores) for secuencia in secuencias)


def tiene_escalera_grande(dados):
    """True si los dados son 1-2-3-4-5 o 2-3-4-5-6."""
    valores = set(dados)
    return valores == {1, 2, 3, 4, 5} or valores == {2, 3, 4, 5, 6}


def calcular_puntuacion(categoria, dados):
    """Calcula los puntos de una categoría sin modificar el marcador."""
    conteo = Counter(dados)
    total = sum(dados)

    if categoria in ("unos", "doses", "treses", "cuatros", "cincos", "seises"):
        valor = UPPER_CATEGORIES.index(categoria) + 1
        return sum(dado for dado in dados if dado == valor)

    if categoria == "trio":
        return total if any(cantidad >= 3 for cantidad in conteo.values()) else 0

    if categoria == "poker":
        return total if any(cantidad >= 4 for cantidad in conteo.values()) else 0

    if categoria == "full":
        cantidades = sorted(conteo.values())
        return 25 if cantidades == [2, 3] else 0

    if categoria == "escalera_pequena":
        return 30 if tiene_escalera_pequena(dados) else 0

    if categoria == "escalera_grande":
        return 40 if tiene_escalera_grande(dados) else 0

    if categoria == "yahtzee":
        return 50 if es_yahtzee(dados) else 0

    if categoria == "azar":
        return total

    raise ValueError(f"Categoría desconocida: {categoria}")


def crear_jugador(nombre):
    """Crea el registro de un jugador con todas las categorías sin usar."""
    return {
        "nombre": nombre,
        "marcador": {categoria: None for categoria in CATEGORIES},
        "bonos_yahtzee": 0,
    }


def puntaje_seccion_superior(jugador):
    """Suma las seis categorías superiores ya registradas."""
    return sum(
        jugador["marcador"][categoria] or 0
        for categoria in UPPER_CATEGORIES
    )


def puntaje_total(jugador):
    """Calcula el total, incluyendo el bono superior y bonos Yahtzee."""
    superior = puntaje_seccion_superior(jugador)
    inferior = sum(
        jugador["marcador"][categoria] or 0
        for categoria in LOWER_CATEGORIES
    )
    bono_superior = 35 if superior >= 63 else 0
    return superior + inferior + bono_superior + jugador["bonos_yahtzee"]


def mostrar_marcador(jugador):
    """Imprime el marcador actual del jugador."""
    print(f"\nMarcador de {jugador['nombre']}:")
    for categoria, nombre in CATEGORIES.items():
        valor = jugador["marcador"][categoria]
        texto = "-" if valor is None else str(valor)
        print(f"  {nombre:<24} {texto:>3}")
    superior = puntaje_seccion_superior(jugador)
    bono = 35 if superior >= 63 else 0
    print(f"  {'Subtotal superior':<24} {superior:>3}")
    print(f"  {'Bono superior':<24} {bono:>3}")
    print(f"  {'Bonos Yahtzee':<24} {jugador['bonos_yahtzee']:>3}")
    print(f"  {'TOTAL ACTUAL':<24} {puntaje_total(jugador):>3}")


def pedir_dados_a_conservar(dados):
    """Solicita posiciones de dados que se conservarán; 0 significa ninguno."""
    while True:
        entrada = input(
            "Escribe las posiciones que quieres conservar (ej. 1,3,5), "
            "o 0 para volver a lanzar todos: "
        ).strip()
        if entrada == "0" or entrada == "":
            return []
        try:
            posiciones = [int(parte.strip()) for parte in entrada.split(",")]
            if len(set(posiciones)) != len(posiciones):
                print("No repitas posiciones.")
                continue
            if any(posicion < 1 or posicion > 5 for posicion in posiciones):
                print("Las posiciones válidas son del 1 al 5.")
                continue
            return [dados[posicion - 1] for posicion in posiciones]
        except ValueError:
            print("Entrada no válida. Usa números separados por comas, por ejemplo 1,3.")


def jugar_turno(jugador):
    """Ejecuta un turno completo y registra una categoría."""
    print(f"\n{'=' * 50}")
    print(f"Turno de {jugador['nombre']}")
    dados = lanzar_dados()
    print(f"Lanzamiento 1: {dados}")

    for numero_lanzamiento in range(2, 4):
        respuesta = input(
            f"¿Quieres volver a lanzar? (s/n) [{numero_lanzamiento - 1} de 2 "
            "relanzamientos disponibles]: "
        ).strip().lower()
        if respuesta != "s":
            break

        conservados = pedir_dados_a_conservar(dados)
        cantidad_nuevos = 5 - len(conservados)
        dados_nuevos = lanzar_dados(cantidad_nuevos)
        dados = conservados + dados_nuevos
        print(f"Lanzamiento {numero_lanzamiento}: {dados}")

    # Bonificación educativa por Yahtzee adicional.
    if es_yahtzee(dados) and jugador["marcador"]["yahtzee"] == 50:
        jugador["bonos_yahtzee"] += 100
        print("¡Yahtzee adicional! Se suman 100 puntos de bonificación.")
        print("Nota: las reglas especiales de comodín no están implementadas.")

    disponibles = [
        categoria for categoria, valor in jugador["marcador"].items()
        if valor is None
    ]

    print("\nPuntuaciones posibles con tus dados:")
    for numero, categoria in enumerate(disponibles, start=1):
        puntos = calcular_puntuacion(categoria, dados)
        print(f"  {numero:>2}. {CATEGORIES[categoria]:<24} {puntos:>3} puntos")

    while True:
        try:
            seleccion = int(input("Elige el número de una categoría: "))
            if 1 <= seleccion <= len(disponibles):
                break
            print("El número está fuera del rango mostrado.")
        except ValueError:
            print("Debes escribir un número entero.")

    categoria_elegida = disponibles[seleccion - 1]
    puntos = calcular_puntuacion(categoria_elegida, dados)
    jugador["marcador"][categoria_elegida] = puntos
    print(
        f"{CATEGORIES[categoria_elegida]}: {puntos} puntos "
        f"registrados para {jugador['nombre']}."
    )


def main():
    """Función principal: organiza la partida entre dos jugadores."""
    print("=" * 50)
    print("           YAHTZEE PARA DOS JUGADORES")
    print("=" * 50)
    nombre1 = input("Nombre del jugador 1: ").strip() or "Jugador 1"
    nombre2 = input("Nombre del jugador 2: ").strip() or "Jugador 2"
    jugadores = [crear_jugador(nombre1), crear_jugador(nombre2)]

    # Hay 13 categorías, por lo que cada jugador juega 13 turnos.
    for ronda in range(1, len(CATEGORIES) + 1):
        print(f"\n\n######## RONDA {ronda} DE {len(CATEGORIES)} ########")
        for jugador in jugadores:
            jugar_turno(jugador)
            mostrar_marcador(jugador)
            input("\nPresiona Enter para continuar...")

    print("\n" + "=" * 50)
    print("                 RESULTADOS FINALES")
    print("=" * 50)
    for jugador in jugadores:
        mostrar_marcador(jugador)

    total1 = puntaje_total(jugadores[0])
    total2 = puntaje_total(jugadores[1])
    if total1 > total2:
        print(f"\n¡Gana {jugadores[0]['nombre']} con {total1} puntos!")
    elif total2 > total1:
        print(f"\n¡Gana {jugadores[1]['nombre']} con {total2} puntos!")
    else:
        print(f"\nLa partida termina en empate: {total1} puntos cada uno.")


if __name__ == "__main__":
    main()
