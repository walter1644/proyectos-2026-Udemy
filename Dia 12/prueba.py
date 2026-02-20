from tkinter import *


#iniciar tkinter
aplicacion = Tk()


#tamaño de la ventana
aplicacion.geometry("180x120") 

#aplicacion.resizable(0,0) #Evitar que se pueda cambiar el tamaño de la ventana


#titulo de la ventana
aplicacion.title("Mi primera ventana")


#color de fondo
aplicacion.config(bg="BlueViolet")


#panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)


#etiqueta titulo
etiqueta_titulo = Label(panel_superior, text="Mi primera ventana", fg="Azure4",
                        font=("Arial", 18),  bg="BurlyWood",width=20)

#posicion de la etiqueta
etiqueta_titulo.grid(row=0, column=0)


#panel izquierdo
panel_izquierdo = Frame(aplicacion, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)


#panel costos
panel_costos = Frame(panel_izquierdo, bd=1, relief=FLAT)
panel_costos.pack(side=BOTTOM)

#panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text="Comidas",
                        bd=1, font=("Arial", 12), relief=FLAT, fg="Azure4", bg="BurlyWood")

panel_comidas.pack(side=LEFT)



#panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text="Bebidas",
                        bd=1, font=("Arial", 12), relief=FLAT, fg="Azure4", bg="BurlyWood")

panel_bebidas.pack(side=LEFT)



#panel postres
panel_postres = LabelFrame(panel_izquierdo, text="Postres",
                        bd=1, font=("Arial", 12), relief=FLAT, fg="Azure4", bg="BurlyWood")

panel_postres.pack(side=LEFT)

#panel derecha
panel_derecho = Frame(aplicacion, bd=1, relief=FLAT)
panel_derecho.pack(side=RIGHT)  

#PANEL CALCULADORA
panel_Calculadora = Frame(panel_derecho, bd=1, relief=FLAT, bg ="BurlyWood")
panel_Calculadora.pack()

#PANEL recibo
panel_recibo = Frame(panel_derecho, bd=1, relief=FLAT, bg ="BurlyWood")
panel_recibo.pack()

#PANEL botones
panel_botones = Frame(panel_derecho, bd=1, relief=FLAT, bg ="BurlyWood")
panel_botones.pack()

lista_comidas = ["Hamburguesa", "Pizza", "Hot Dog"]
lista_bebidas = ["Coca Cola", "Pepsi", "Fanta"]
lista_postres = ["Helado", "Pastel", "Galletas"]



#generar items de comidas
variable_comida=[]
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:

    #crear checkbutton
    variable_comida.append('')
    variable_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                        text=comida.title(),
                        font=("Arial", 12),
                        bg="BurlyWood",
                        onvalue=1,
                        offvalue=0)
    comida.grid(row=contador, column=0, sticky=W)

    #crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                    font=("Arial", 12, 'bold'),
                                    bd=5,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador, column=1)
    contador += 1 


#generar items de bebidas
variable_bebida=[]
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:

    #crear checkbutton
    variable_bebida.append('')
    variable_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                        text=bebida.title(),
                        font=("Arial", 12),
                        bg="BurlyWood",
                        onvalue=1,
                        offvalue=0)
    bebida.grid(row=contador, column=0, sticky=W)

    #crear cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                    font=("Arial", 12, 'bold'),
                                    bd=5,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador, column=1)
    contador += 1


#generar los checkbutton de postres
variable_postre=[]
cuadros_postre = []
texto_postre = []
contador = 0
for postre in lista_postres:

    #crear checkbutton
    variable_postre.append('')
    variable_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres,
                        text=postre.title(),
                        font=("Arial", 12),
                        bg="BurlyWood",
                        onvalue=1,
                        offvalue=0)
    postre.grid(row=contador, column=0, sticky=W)

    #crear cuadros de entrada
    cuadros_postre.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postre[contador] = Entry(panel_postres,
                                    font=("Arial", 12, 'bold'),
                                    bd=5,
                                    width=6,
                                    state=DISABLED,
                                    textvariable=texto_postre[contador])
    cuadros_postre[contador].grid(row=contador, column=1)
    contador += 1

#Evitar la ventana se cierre  
aplicacion.mainloop()