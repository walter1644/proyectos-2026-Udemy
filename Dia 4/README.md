# sistema_prendas.py — Documentación

## Descripción ✅
Juego de adivinanza en el que el programa piensa en una prenda de una lista y el jugador tiene hasta 8 intentos para adivinarla.

---

## Cómo funciona ⚙️
- Se define la lista `prendas` con varias opciones (p. ej. `remera`, `pantalon`, `campera`, ...).
- El programa elige aleatoriamente una prenda secreta con `randint`.
- Pide el nombre del jugador y valida que contenga **solo letras y espacios**; luego lo normaliza con `title()`.
- Muestra la lista de prendas y permite hasta 8 intentos.
- En cada intento, el jugador introduce una prenda (se convierte a minúsculas y se elimina espacio alrededor).
  - Si la prenda no está en la lista, se informa y se cuenta como intento.
  - Si la prenda está antes o después alfabéticamente, se indica la dirección.
  - Tras cada intento incorrecto se muestra una pista: **letra inicial** y **longitud** (por ejemplo: `Pista: Empieza con 'c' y tiene 7 letras.`).
- Si el jugador acierta se muestra un mensaje de felicitación con los intentos usados.
- Si se agotan los intentos, se revela la prenda secreta.

---

## Validaciones y detalles técnicos 🔒
- **Nombre:** `nombre.replace(' ', '').isalpha()` — permite letras Unicode (acentos, ñ) y espacios.
- **Prenda:** se valida que la entrada esté en la lista `prendas`.
- Las pistas siempre muestran la primera letra y la longitud (maneja singular/plural).

---

## Ejemplos de entrada y salida 🧪
- Nombre válido: `Ana María` → aceptado, mostrado como `Ana María`.
- Nombre inválido: `Juan123` → se solicita reintento.
- Prenda no listada: `zapato` → `Esa prenda no está en la lista`.
- Pista mostrada: `Pista: Empieza con 'c' y tiene 7 letras.`

---

## Mejoras sugeridas ✨
- Mostrar la pista solo a partir del 2º/3º intento.
- Permitir guiones o apóstrofes en el nombre (p. ej. `María-José`).
- Implementar pistas tipo "letras en la posición correcta" (estilo Mastermind).

---