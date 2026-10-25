# Yahtzee para dos jugadores (Python)

Proyecto académico que implementa una versión de consola del juego clásico Yahtzee.

## Requisitos
- Python 3.9 o superior
- No requiere instalar paquetes externos

## Cómo ejecutar
Desde la carpeta raíz del proyecto:

```bash
python src/yahtzee.py
```

En algunos sistemas puede ser necesario usar `python3` en lugar de `python`.

## Cómo ejecutar las pruebas
Desde la carpeta raíz:

```bash
python -m unittest discover -s tests -v
```

## Reglas implementadas
- Dos jugadores alternan turnos.
- Cinco dados de seis caras y hasta tres lanzamientos por turno.
- Se pueden conservar dados por posición y relanzar el resto.
- Las 13 categorías clásicas de puntuación.
- Bono de 35 puntos cuando la sección superior suma 63 o más.
- Bono de 100 puntos por Yahtzees adicionales cuando la categoría Yahtzee ya obtuvo 50 puntos.
- Gana el jugador con mayor puntaje final; se informa empate si corresponde.

## Alcance y limitación conocida
Para mantener el programa apropiado para principiantes, no se implementan las reglas especiales de comodín (*Joker rules*) de la versión oficial cuando se obtiene un Yahtzee adicional. En ese caso se aplica el bono de 100 puntos y la categoría seleccionada se calcula con sus reglas normales. Esta decisión se documenta como una simplificación del modelo.

## Estructura
- `src/yahtzee.py`: código principal del juego.
- `tests/test_yahtzee.py`: pruebas automáticas de puntuación.
- `docs/documento_tecnico.docx`: documento técnico del proyecto.
- `docs/guia_pruebas.md`: casos de prueba manuales y automáticos.

## Distribución aleatoria
Cada dado se genera con `random.randint(1, 6)`. La función asigna la misma probabilidad teórica a cada cara: 1/6, suponiendo el generador pseudoaleatorio de Python como mecanismo de simulación.

## Autoría
Completa este apartado con tu nombre, curso, docente e institución antes de entregar.
