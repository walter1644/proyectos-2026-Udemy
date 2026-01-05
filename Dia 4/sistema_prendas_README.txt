sistema_prendas.py — Explicación y uso

Descripción
-----------
Este script es un juego de adivinanza en el que el programa piensa en una prenda de una lista predefinida y el usuario trata de adivinarla en hasta 8 intentos.

Cómo funciona
-------------
1. Se define una lista llamada `prendas` con varias opciones (ej.: "remera", "pantalon", ...).
2. El programa elige aleatoriamente una prenda secreta con `randint`.
3. Pide el nombre del jugador y valida que contenga solo letras y espacios. Si la entrada es inválida pide reintentar.
   - La validación permite letras acentuadas y la letra "ñ".
   - El nombre se normaliza con `title()`.
4. Muestra la lista de prendas y los intentos permitidos (8).
5. En cada intento el jugador introduce el nombre de una prenda (se transforma a minúsculas y se quitan espacios alrededor).
   - Si la prenda no está en la lista, muestra "Esa prenda no está en la lista" y se cuenta como intento.
   - Si la prenda está antes o después en orden alfabético, muestra una pista correspondiente.
   - Tras cada intento incorrecto también muestra una pista adicional:
     "Pista: Empieza con 'x' y tiene N letras." (se ajusta la palabra "letra"/"letras").
6. Si el jugador acierta se muestra un mensaje de felicitación con el número de intentos.
7. Si se agotaron los 8 intentos sin acertar, se revela la prenda secreta.

Detalles técnicos y validaciones
--------------------------------
- Validación de nombre: se usa `nombre.replace(' ', '').isalpha()` para garantizar solo letras y espacios.
- Validación de prenda: se comprueba si la entrada está en la lista `prendas`.
- Las pistas son siempre la primera letra de la prenda secreta y su longitud (en letras).

Ejemplos de uso
---------------
- Entrada de nombre válida: "Ana María" → aceptado y mostrado como "Ana María".
- Entrada de nombre inválida: "Juan123" → el programa pide reintentar.
- Entrada de prenda no lista: "zapato" → "Esa prenda no está en la lista".
- Pista mostrada: "Pista: Empieza con 'c' y tiene 7 letras." 

Posibles mejoras
----------------
- Mostrar la pista solo a partir del 2º o 3º intento.
- Permitir guiones o apóstrofes en el nombre (p. ej. "María-José").
- Implementar una pista que muestre letras correctas en la posición (similar a Mastermind).
