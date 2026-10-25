Guía de pruebas
Pruebas automáticas
Ejecutar:

python -m unittest discover -s tests -v
Las pruebas verifican categorías superiores, trío, full house, escaleras, Yahtzee, azar y bonificación superior.

Pruebas manuales sugeridas
Caso	Entrada/condición	Resultado esperado
Lanzamiento	Iniciar un turno	Se muestran cinco valores entre 1 y 6
Conservar dados	Ingresar 1,3	Se mantienen los dados en posiciones 1 y 3
Volver a lanzar todos	Ingresar 0	Se generan cinco dados nuevos
Categoría ya usada	Intentar elegir una categoría ya registrada	No aparece entre las opciones disponibles
Unos	Dados [1,1,3,4,6]	2 puntos en Unos
Trío	Dados [2,2,2,4,5]	15 puntos en Trío
Full house	Dados [3,3,3,5,5]	25 puntos
Escalera pequeña	Dados [1,2,2,3,4]	30 puntos
Escalera grande	Dados [2,3,4,5,6]	40 puntos
Yahtzee	Dados [6,6,6,6,6]	50 puntos si se selecciona Yahtzee libre
Bono superior	Categorías superiores suman 63	35 puntos adicionales
Fin de partida	Ambos completan 13 categorías	Se muestra el total y ganador/empate
Las pruebas manuales se deben realizar y registrar durante la ejecución real. No se deben presentar como ejecutadas si no se han llevado a cabo.
