# ─── Lógica de Negocio ───────────────────────────────────────────────────────
import random
import datetime
from tkinter import filedialog, messagebox

from datos import (
    precios_comida, precios_bebida, precios_postres,
    lista_comidas, lista_bebidas, lista_postres,
    TASA_IMPUESTO,
)

# ── Calculadora ───────────────────────────────────────────────────────────────

operador = ''


def click_boton(numero, visor):
    global operador
    operador += numero
    visor.delete(0, 'end')
    visor.insert('end', operador)


def borrar(visor):
    global operador
    operador = ''
    visor.delete(0, 'end')


def obtener_resultado(visor):
    global operador
    try:
        resultado = str(eval(operador))
        visor.delete(0, 'end')
        visor.insert(0, resultado)
    except Exception:
        visor.delete(0, 'end')
        visor.insert(0, 'Error')
    operador = ''


# ── Pedido ────────────────────────────────────────────────────────────────────

def revisar_check(variables_comida, cuadros_comida, texto_comida,
                  variables_bebida, cuadros_bebida, texto_bebida,
                  variables_postres, cuadros_postres, texto_postres):
    """Habilita/deshabilita los campos de cantidad según los checks."""
    for grupo_vars, grupo_cuadros, grupo_textos in [
        (variables_comida,  cuadros_comida,  texto_comida),
        (variables_bebida,  cuadros_bebida,  texto_bebida),
        (variables_postres, cuadros_postres, texto_postres),
    ]:
        for i, var in enumerate(grupo_vars):
            if var.get() == 1:
                grupo_cuadros[i].config(state='normal')
                if grupo_cuadros[i].get() == '0':
                    grupo_cuadros[i].delete(0, 'end')
                grupo_cuadros[i].focus()
            else:
                grupo_cuadros[i].config(state='disabled')
                grupo_textos[i].set('0')


def calcular_total(texto_comida, texto_bebida, texto_postres):
    """Devuelve un dict con los subtotales, impuestos y total."""
    def subtotal(textos, precios):
        return sum(float(t.get()) * p for t, p in zip(textos, precios))

    st_comida  = subtotal(texto_comida,  precios_comida)
    st_bebida  = subtotal(texto_bebida,  precios_bebida)
    st_postres = subtotal(texto_postres, precios_postres)
    sub_total  = st_comida + st_bebida + st_postres
    impuestos  = sub_total * TASA_IMPUESTO
    total      = sub_total + impuestos

    return {
        'comida':   round(st_comida,  2),
        'bebida':   round(st_bebida,  2),
        'postres':  round(st_postres, 2),
        'subtotal': round(sub_total,  2),
        'impuestos':round(impuestos,  2),
        'total':    round(total,      2),
    }


# ── Recibo ────────────────────────────────────────────────────────────────────

def generar_recibo(texto_recibo, texto_comida, texto_bebida, texto_postres, totales):
    """Escribe el recibo en el widget Text."""
    texto_recibo.delete(1.0, 'end')
    num_recibo  = f'N# - {random.randint(1000, 9999)}'
    fecha       = datetime.datetime.now()
    fecha_str   = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'

    texto_recibo.insert('end', f'Datos:\t{num_recibo}\t\t{fecha_str}\n')
    texto_recibo.insert('end', '*' * 47 + '\n')
    texto_recibo.insert('end', 'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert('end', '-' * 54 + '\n')

    for i, t in enumerate(texto_comida):
        if t.get() != '0':
            texto_recibo.insert('end',
                f'{lista_comidas[i]}\t\t{t.get()}\t$ {int(t.get()) * precios_comida[i]}\n')

    for i, t in enumerate(texto_bebida):
        if t.get() != '0':
            texto_recibo.insert('end',
                f'{lista_bebidas[i]}\t\t{t.get()}\t$ {int(t.get()) * precios_bebida[i]}\n')

    for i, t in enumerate(texto_postres):
        if t.get() != '0':
            texto_recibo.insert('end',
                f'{lista_postres[i]}\t\t{t.get()}\t$ {int(t.get()) * precios_postres[i]}\n')

    texto_recibo.insert('end', '-' * 54 + '\n')
    texto_recibo.insert('end', f' Costo de la Comida: \t\t\t$ {totales["comida"]}\n')
    texto_recibo.insert('end', f' Costo de la Bebida: \t\t\t$ {totales["bebida"]}\n')
    texto_recibo.insert('end', f' Costo de la Postres: \t\t\t$ {totales["postres"]}\n')
    texto_recibo.insert('end', '-' * 54 + '\n')
    texto_recibo.insert('end', f' Sub-total: \t\t\t$ {totales["subtotal"]}\n')
    texto_recibo.insert('end', f' Impuestos: \t\t\t$ {totales["impuestos"]}\n')
    texto_recibo.insert('end', f' Total: \t\t\t$ {totales["total"]}\n')
    texto_recibo.insert('end', '*' * 47 + '\n')
    texto_recibo.insert('end', 'Lo esperamos pronto')


def guardar_recibo(texto_recibo):
    """Guarda el contenido del recibo en un archivo .txt."""
    info = texto_recibo.get(1.0, 'end')
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if archivo:
        archivo.write(info)
        archivo.close()
        messagebox.showinfo('Informacion', 'Su recibo ha sido guardado')


def resetear_todo(texto_recibo,
                  texto_comida, cuadros_comida, variables_comida,
                  texto_bebida, cuadros_bebida, variables_bebida,
                  texto_postres, cuadros_postres, variables_postres,
                  vars_display):
    """Limpia recibo, cantidades, checks y campos de totales."""
    texto_recibo.delete(1.0, 'end')

    for textos, cuadros, variables in [
        (texto_comida,  cuadros_comida,  variables_comida),
        (texto_bebida,  cuadros_bebida,  variables_bebida),
        (texto_postres, cuadros_postres, variables_postres),
    ]:
        for t in textos:
            t.set('0')
        for c in cuadros:
            c.config(state='disabled')
        for v in variables:
            v.set(0)

    for v in vars_display.values():
        v.set('')
