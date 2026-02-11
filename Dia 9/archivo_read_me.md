# 📘 README – Buscador de Números de Serie

## 📌 Descripción
Este programa recorre un directorio y sus subcarpetas, abre cada archivo de texto y busca patrones que coincidan con un número de serie definido por una expresión regular. Finalmente, muestra los resultados en una tabla junto con la fecha y la duración de la búsqueda.

---

## ⚙️ Funcionamiento paso a paso
1. **Inicio del programa**
   - Se importan los módulos necesarios (`re`, `os`, `time`, `datetime`, `Path`, `math`).
   - Se guarda el tiempo inicial de ejecución.
   - Se define la ruta del directorio a analizar.
   - Se establece el patrón regex: `N\D{3}-\d{5}`.

2. **Funciones principales**
   - **`buscar_numero(archivo, patron)`**  
     Abre un archivo, lee su contenido y busca el patrón.  
     Si lo encuentra, devuelve el resultado; si no, devuelve vacío.
   
   - **`crear_listas()`**  
     Recorre todos los archivos del directorio usando `Path.rglob`.  
     Si encuentra coincidencias, guarda el número de serie y el nombre del archivo en listas paralelas.
   
   - **`mostrar_todo()`**  
     Muestra los resultados en formato tabla.  
     Si no se encuentra nada, imprime un mensaje de aviso.  
     También muestra la cantidad de coincidencias y el tiempo total de ejecución.

3. **Ejecución**
   - Se llama a `crear_listas()` para generar las listas de resultados.
   - Se llama a `mostrar_todo()` para imprimir la salida final.

---

## 📊 Diagrama de flujo

```text
 ┌─────────────────────┐
 │   Inicio del script │
 └───────┬─────────────┘
         │
         ▼
 ┌─────────────────────┐
 │ Definir ruta y      │
 │ patrón regex        │
 └───────┬─────────────┘
         │
         ▼
 ┌─────────────────────┐
 │ crear_listas()      │
 │ - Recorre archivos  │
 │ - Llama buscar_numero│
 │ - Guarda resultados │
 └───────┬─────────────┘
         │
         ▼
 ┌─────────────────────┐
 │ mostrar_todo()      │
 │ ¿Hay resultados?    │
 └───────┬─────────────┘
         │
   ┌─────┴─────┐
   │           │
   ▼           ▼
┌─────────┐ ┌─────────────────────┐
│ No hay  │ │ Sí hay resultados   │
│ datos   │ │ - Imprime tabla     │
│ encontrados │ - Muestra cantidad│
└─────────┘ │ - Muestra duración  │
            └─────────────────────┘
                     │
                     ▼
           ┌─────────────────────┐
           │ Fin del programa    │
           └─────────────────────┘

--------------------------------------------------
Fecha de búsqueda: 10/2/2026

ARCHIVO                 NRO. SERIE
-------                 ----------
ejemplo.txt             NABC-12345

Números encontrados: 1
Duración de la búsqueda: 3 segundos
--------------------------------------------------
