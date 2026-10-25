import unittest
from src.yahtzee import (
    calcular_puntuacion,
    crear_jugador,
    es_yahtzee,
    tiene_escalera_pequena,
    tiene_escalera_grande,
    puntaje_total,
    puntaje_seccion_superior,
)


class TestYahtzee(unittest.TestCase):
    def test_unos(self):
        self.assertEqual(calcular_puntuacion("unos", [1, 1, 3, 4, 6]), 2)

    def test_trio(self):
        self.assertEqual(calcular_puntuacion("trio", [2, 2, 2, 4, 5]), 15)
        self.assertEqual(calcular_puntuacion("trio", [2, 2, 3, 4, 5]), 0)

    def test_full_house(self):
        self.assertEqual(calcular_puntuacion("full", [3, 3, 3, 5, 5]), 25)
        self.assertEqual(calcular_puntuacion("full", [3, 3, 3, 3, 5]), 0)

    def test_escaleras(self):
        self.assertTrue(tiene_escalera_pequena([1, 2, 2, 3, 4]))
        self.assertTrue(tiene_escalera_grande([2, 3, 4, 5, 6]))
        self.assertFalse(tiene_escalera_grande([1, 2, 3, 4, 6]))

    def test_yahtzee(self):
        self.assertTrue(es_yahtzee([6, 6, 6, 6, 6]))
        self.assertEqual(calcular_puntuacion("yahtzee", [6, 6, 6, 6, 6]), 50)

    def test_azar(self):
        self.assertEqual(calcular_puntuacion("azar", [1, 2, 3, 4, 5]), 15)

    def test_bono_superior(self):
        jugador = crear_jugador("Prueba")
        for categoria, puntos in zip(
            ["unos", "doses", "treses", "cuatros", "cincos", "seises"],
            [3, 6, 9, 12, 15, 18],
        ):
            jugador["marcador"][categoria] = puntos
        self.assertEqual(puntaje_seccion_superior(jugador), 63)
        self.assertEqual(puntaje_total(jugador), 98)  # 63 + 35 de bono


if __name__ == "__main__":
    unittest.main()
