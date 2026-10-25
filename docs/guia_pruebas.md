# Guía de pruebas - Yahtzee

## Objetivo
Verificar que las funciones principales del juego Yahtzee funcionen correctamente.

## Pruebas recomendadas

1. Ejecutar el juego con el comando `python src/yahtzee.py`.
2. Comprobar que se muestran dos jugadores.
3. Verificar que cada turno permite lanzar los dados y conservar dados entre lanzamientos.
4. Comprobar que se puede seleccionar una categoría de puntuación.
5. Verificar que las puntuaciones se acumulen correctamente.
6. Comprobar que el juego termina después de completar las categorías.
7. Ejecutar las pruebas automatizadas con `python -m unittest discover -s tests -v`.

## Resultado esperado
El juego debe permitir jugar por turnos, registrar las puntuaciones y determinar el ganador. Las pruebas automatizadas deben finalizar sin errores.

