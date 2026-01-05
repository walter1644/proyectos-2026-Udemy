def pedir_texto(parametro):
    while True:
        variable_local = input(parametro).strip().title()
        if variable_local and variable_local.replace(" ", "").isalpha():
            return variable_local
        print("Por favor ingrese solo letras (sin números).")

color = pedir_texto("Ingrese el nombre de su color favorito: ")
ciudad = pedir_texto("Ingrese la ciudad que le gustaria visitar: ")
print(f"El nombre de su cerveza es: '{color} {ciudad}'")