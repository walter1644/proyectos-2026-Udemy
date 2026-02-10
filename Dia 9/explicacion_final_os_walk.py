"""
A QUÉ CARPETA VA DIRIGIDA CADA VARIABLE - EXPLICACIÓN VISUAL
=============================================================

La estructura de carpetas es:

Mi_Gran_Directorio/
│
├── texto1.txt
├── texto2.txt
│
├── Carpeta_A/
│   ├── texto3.txt
│   ├── texto4.txt
│   └── SubCarpeta_X/
│       └── texto5.txt
│
└── Carpeta_B/
    └── texto6.txt


═══════════════════════════════════════════════════════════════════════════════
ITERACIÓN 1 - Estoy en la CARPETA RAÍZ
═══════════════════════════════════════════════════════════════════════════════

    ┌─ Estoy AQUÍ ahora
    │
    ▼
Mi_Gran_Directorio/  ◄─── carpeta = '/home/claude/Mi_Gran_Directorio'
│
├── texto1.txt       ◄─┐
├── texto2.txt       ◄─┤─── archivo = ['texto1.txt', 'texto2.txt']
│                      │    (archivos que están AQUÍ DENTRO)
├── Carpeta_A/       ◄─┤
└── Carpeta_B/       ◄─┴─── subcarpeta = ['Carpeta_A', 'Carpeta_B']
                            (carpetas que están AQUÍ DENTRO)

RESUMEN ITERACIÓN 1:
--------------------
carpeta    → La ruta de donde ESTOY PARADO ahora (Mi_Gran_Directorio)
subcarpeta → Las carpetas que VEO dentro (Carpeta_A, Carpeta_B)
archivo    → Los archivos que VEO dentro (texto1.txt, texto2.txt)


═══════════════════════════════════════════════════════════════════════════════
ITERACIÓN 2 - Ahora ENTRÉ a Carpeta_A
═══════════════════════════════════════════════════════════════════════════════

Mi_Gran_Directorio/
│
│       ┌─ Ahora estoy AQUÍ
│       │
├── Carpeta_A/  ◄─── carpeta = '/home/claude/Mi_Gran_Directorio/Carpeta_A'
│   │
│   ├── texto3.txt       ◄─┐
│   ├── texto4.txt       ◄─┤─── archivo = ['texto3.txt', 'texto4.txt']
│   │                      │    (archivos que están AQUÍ DENTRO)
│   └── SubCarpeta_X/    ◄─┴─── subcarpeta = ['SubCarpeta_X']
│                               (carpetas que están AQUÍ DENTRO)
│
└── Carpeta_B/

RESUMEN ITERACIÓN 2:
--------------------
carpeta    → La ruta de donde ESTOY PARADO ahora (Carpeta_A)
subcarpeta → Las carpetas que VEO dentro (SubCarpeta_X)
archivo    → Los archivos que VEO dentro (texto3.txt, texto4.txt)


═══════════════════════════════════════════════════════════════════════════════
ITERACIÓN 3 - Ahora ENTRÉ a SubCarpeta_X
═══════════════════════════════════════════════════════════════════════════════

Mi_Gran_Directorio/
│
├── Carpeta_A/
│   │
│   │           ┌─ Ahora estoy AQUÍ
│   │           │
│   └── SubCarpeta_X/  ◄─── carpeta = '.../Carpeta_A/SubCarpeta_X'
│       │
│       └── texto5.txt ◄─── archivo = ['texto5.txt']
│                           (archivos que están AQUÍ DENTRO)
│                           
│                           subcarpeta = []
│                           (NO hay carpetas aquí dentro)
│
└── Carpeta_B/

RESUMEN ITERACIÓN 3:
--------------------
carpeta    → La ruta de donde ESTOY PARADO ahora (SubCarpeta_X)
subcarpeta → Las carpetas que VEO dentro (ninguna, lista vacía [])
archivo    → Los archivos que VEO dentro (texto5.txt)


═══════════════════════════════════════════════════════════════════════════════
ITERACIÓN 4 - Ahora ENTRÉ a Carpeta_B
═══════════════════════════════════════════════════════════════════════════════

Mi_Gran_Directorio/
│
├── Carpeta_A/
│
│       ┌─ Ahora estoy AQUÍ
│       │
└── Carpeta_B/  ◄─── carpeta = '/home/claude/Mi_Gran_Directorio/Carpeta_B'
    │
    └── texto6.txt ◄─── archivo = ['texto6.txt']
                        (archivos que están AQUÍ DENTRO)
                        
                        subcarpeta = []
                        (NO hay carpetas aquí dentro)

RESUMEN ITERACIÓN 4:
--------------------
carpeta    → La ruta de donde ESTOY PARADO ahora (Carpeta_B)
subcarpeta → Las carpetas que VEO dentro (ninguna, lista vacía [])
archivo    → Los archivos que VEO dentro (texto6.txt)


═══════════════════════════════════════════════════════════════════════════════
CONCLUSIÓN - LA RESPUESTA A TU PREGUNTA
═══════════════════════════════════════════════════════════════════════════════

¿A qué carpeta van dirigidas cada variable?

┌─────────────┬──────────────────────────────────────────────────────────────┐
│  VARIABLE   │  A QUÉ CARPETA VA DIRIGIDA                                   │
├─────────────┼──────────────────────────────────────────────────────────────┤
│  carpeta    │  A la carpeta donde ESTOY PARADO EN ESTE MOMENTO            │
│             │  (cambia en cada iteración del for)                         │
├─────────────┼──────────────────────────────────────────────────────────────┤
│  subcarpeta │  A las SUBCARPETAS que están DENTRO de donde estoy parado   │
│             │  (es decir, dentro de 'carpeta')                            │
├─────────────┼──────────────────────────────────────────────────────────────┤
│  archivo    │  A los ARCHIVOS que están DENTRO de donde estoy parado      │
│             │  (es decir, dentro de 'carpeta')                            │
└─────────────┴──────────────────────────────────────────────────────────────┘


ANALOGÍA SIMPLE:
----------------

Imagina que eres un cartero que tiene que visitar todas las casas de un edificio:

carpeta    = "En qué piso estoy parado AHORA"
subcarpeta = "Qué escaleras veo que bajan desde aquí"
archivo    = "Qué cartas tengo que repartir en ESTE piso"

En cada piso que visitas (cada iteración):
- Sabes en qué piso estás (carpeta)
- Ves qué escaleras hay hacia otros pisos (subcarpeta)
- Repartes las cartas de ese piso (archivo)

¡Y luego bajas al siguiente piso y repites!


REGLA DE ORO:
-------------

Las 3 variables SIEMPRE se refieren a LA MISMA UBICACIÓN:
    
    carpeta    ───┐
                  │
    subcarpeta ───┼──► Todas hablan de LO QUE HAY en la MISMA carpeta
                  │
    archivo    ───┘

Solo que 'carpeta' es la DIRECCIÓN, y las otras dos son LISTAS de lo que hay adentro.

"""
