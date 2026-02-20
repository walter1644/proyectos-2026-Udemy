# ─── Interfaz Gráfica ────────────────────────────────────────────────────────
from tkinter import *

from datos import lista_comidas, lista_bebidas, lista_postres
import logica


def construir_ui(app):
    """
    Construye todos los widgets de la aplicación sobre la ventana `app` (Tk).
    Devuelve un dict con las referencias necesarias para la lógica.
    """

    # ── Configuración general ─────────────────────────────────────────────────
    app.geometry('1020x630+0+0')
    app.resizable(0, 0)
    app.title('Mi Restaurante - Sistema de Facturacion')
    app.config(bg='burlywood')

    # ── Paneles ───────────────────────────────────────────────────────────────
    panel_superior = Frame(app, bd=1, relief=FLAT)
    panel_superior.pack(side=TOP)

    panel_izquierdo = Frame(app, bd=1, relief=FLAT)
    panel_izquierdo.pack(side=LEFT)

    panel_costos  = Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=50)
    panel_costos.pack(side=BOTTOM)

    panel_comidas = LabelFrame(panel_izquierdo, text='Comida',   font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
    panel_comidas.pack(side=LEFT)

    panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas',  font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
    panel_bebidas.pack(side=LEFT)

    panel_postres = LabelFrame(panel_izquierdo, text='Postres',  font=('Dosis', 19, 'bold'), bd=1, relief=FLAT, fg='azure4')
    panel_postres.pack(side=LEFT)

    panel_derecha      = Frame(app, bd=1, relief=FLAT)
    panel_derecha.pack(side=RIGHT)

    panel_calculadora  = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
    panel_calculadora.pack()

    panel_recibo       = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
    panel_recibo.pack()

    panel_botones      = Frame(panel_derecha, bd=1, relief=FLAT, bg='burlywood')
    panel_botones.pack()

    # ── Título ────────────────────────────────────────────────────────────────
    Label(panel_superior, text='Sistema de Facturacion',
          fg='azure4', font=('Dosis', 58), bg='burlywood', width=27).grid(row=0, column=0)

    # ── Generador de filas de producto ────────────────────────────────────────
    def crear_filas_producto(panel, lista):
        variables, cuadros, textos = [], [], []
        for i, nombre in enumerate(lista):
            var = IntVar()
            variables.append(var)

            check = Checkbutton(panel, text=nombre.title(),
                                font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0,
                                variable=var, command=lambda: _revisar())
            check.grid(row=i, column=0, sticky=W)

            txt = StringVar(value='0')
            textos.append(txt)

            entry = Entry(panel, font=('Dosis', 18, 'bold'), bd=1,
                          width=6, state=DISABLED, textvariable=txt)
            entry.grid(row=i, column=1)
            cuadros.append(entry)

        return variables, cuadros, textos

    variables_comida,  cuadros_comida,  texto_comida  = crear_filas_producto(panel_comidas,  lista_comidas)
    variables_bebida,  cuadros_bebida,  texto_bebida  = crear_filas_producto(panel_bebidas,  lista_bebidas)
    variables_postres, cuadros_postres, texto_postres = crear_filas_producto(panel_postres,  lista_postres)

    # Callback de checks (necesita acceso a las listas ya creadas)
    def _revisar():
        logica.revisar_check(
            variables_comida,  cuadros_comida,  texto_comida,
            variables_bebida,  cuadros_bebida,  texto_bebida,
            variables_postres, cuadros_postres, texto_postres,
        )

    # Reasignar el command correcto a los Checkbuttons ya creados
    # (el lambda dentro de crear_filas_producto captura _revisar por nombre)

    # ── Variables de totales ──────────────────────────────────────────────────
    var_costo_comida  = StringVar()
    var_costo_bebida  = StringVar()
    var_costo_postres = StringVar()
    var_subtotal      = StringVar()
    var_impuestos     = StringVar()
    var_total         = StringVar()

    vars_display = {
        'comida':    var_costo_comida,
        'bebida':    var_costo_bebida,
        'postres':   var_costo_postres,
        'subtotal':  var_subtotal,
        'impuestos': var_impuestos,
        'total':     var_total,
    }

    # ── Panel de costos ───────────────────────────────────────────────────────
    def lbl_entry(panel, texto, var, row, col_lbl, col_entry):
        Label(panel, text=texto, font=('Dosis', 12, 'bold'),
              bg='azure4', fg='white').grid(row=row, column=col_lbl)
        Entry(panel, font=('Dosis', 12, 'bold'), bd=1, width=10,
              state='readonly', textvariable=var).grid(row=row, column=col_entry, padx=41)

    lbl_entry(panel_costos, 'Costo Comida',  var_costo_comida,  0, 0, 1)
    lbl_entry(panel_costos, 'Costo Bebida',  var_costo_bebida,  1, 0, 1)
    lbl_entry(panel_costos, 'Costo Postres', var_costo_postres, 2, 0, 1)
    lbl_entry(panel_costos, 'Subtotal',      var_subtotal,      0, 2, 3)
    lbl_entry(panel_costos, 'Impuestos',     var_impuestos,     1, 2, 3)
    lbl_entry(panel_costos, 'Total',         var_total,         2, 2, 3)

    # ── Área de recibo ────────────────────────────────────────────────────────
    texto_recibo = Text(panel_recibo, font=('Dosis', 12, 'bold'), bd=1, width=42, height=10)
    texto_recibo.grid(row=0, column=0)

    # ── Calculadora ───────────────────────────────────────────────────────────
    visor = Entry(panel_calculadora, font=('Dosis', 16, 'bold'), width=32, bd=1)
    visor.grid(row=0, column=0, columnspan=4)

    botones_calc = ['7', '8', '9', '+', '4', '5', '6', '-',
                    '1', '2', '3', 'x', 'R', 'B', '0', '/']
    guardados = []
    fila, columna = 1, 0
    for b in botones_calc:
        btn = Button(panel_calculadora, text=b.title(),
                     font=('Dosis', 16, 'bold'), fg='white', bg='azure4', bd=1, width=8)
        guardados.append(btn)
        btn.grid(row=fila, column=columna)
        columna += 1
        if columna == 4:
            columna = 0
            fila += 1

    digitos = ['7','8','9','+','4','5','6','-','1','2','3','*','','','0','/']
    for i, d in enumerate(digitos):
        if d:
            guardados[i].config(command=lambda n=d: logica.click_boton(n, visor))
    guardados[12].config(command=lambda: logica.obtener_resultado(visor))
    guardados[13].config(command=lambda: logica.borrar(visor))

    # ── Botones principales ───────────────────────────────────────────────────
    def _total():
        totales = logica.calcular_total(texto_comida, texto_bebida, texto_postres)
        var_costo_comida.set(f'$ {totales["comida"]}')
        var_costo_bebida.set(f'$ {totales["bebida"]}')
        var_costo_postres.set(f'$ {totales["postres"]}')
        var_subtotal.set(f'$ {totales["subtotal"]}')
        var_impuestos.set(f'$ {totales["impuestos"]}')
        var_total.set(f'$ {totales["total"]}')

    def _recibo():
        totales = logica.calcular_total(texto_comida, texto_bebida, texto_postres)
        logica.generar_recibo(texto_recibo, texto_comida, texto_bebida, texto_postres, totales)

    def _guardar():
        logica.guardar_recibo(texto_recibo)

    def _resetear():
        logica.resetear_todo(
            texto_recibo,
            texto_comida,  cuadros_comida,  variables_comida,
            texto_bebida,  cuadros_bebida,  variables_bebida,
            texto_postres, cuadros_postres, variables_postres,
            vars_display,
        )

    acciones = [('Total', _total), ('Recibo', _recibo), ('Guardar', _guardar), ('Resetear', _resetear)]
    for col, (nombre, cmd) in enumerate(acciones):
        Button(panel_botones, text=nombre, font=('Dosis', 14, 'bold'),
               fg='white', bg='azure4', bd=1, width=9, command=cmd).grid(row=0, column=col)
