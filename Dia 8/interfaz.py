class InterfazUsuario:  # Define clase para manejo de interfaz
    """Maneja la interfaz de usuario y validación de entradas"""
    
    @staticmethod  # Decorador que indica método estático
    def mostrar_menu(areas_disponibles: dict):  # Método que muestra menú y recibe un diccionario
        """Muestra el menú de opciones"""
        print("\n" + "=" * 50)  # Línea superior
        print("\t BIENVENIDO A FARMACIA PYTHON")  # Título centrado
        print("=" * 50)  # Línea decorativa
        print("\n📋 SACAR TURNO:")  # Sección de sacar turno
        opciones = " | ".join([f"[{codigo_area}] {nombre_area}" for codigo_area, nombre_area in areas_disponibles.items()])# Crea string con todas las áreas separadas por " | ", ej: "[P] Perfumería | [F] Farmacia | [C] Cosmética"
        print(f"  {opciones}")  # Imprime opciones
        
        print("\n🔔 LLAMAR TURNO:")  # Sección de llamar turno
        print("[1] Perfumería | [2] Farmacia | [3] Cosmética")  # Opciones de llamada
        
        print("\n📊 INFORMACIÓN:")  # Sección de información
        print("[T] - Ver turnos | [E] - Ver estadísticas | [S] - Salir")  # Opciones info
        print("=" * 40)  # Línea de cierre
    
    @staticmethod  # Método estático
    def solicitar_opcion(mensaje: str, opciones_validas: list) -> str:  # Solicita y valida opción
        """Solicita una opción al usuario con validación"""
        while True:  # Bucle infinito hasta obtener opción válida
            try:  # Intenta ejecutar
                opcion = input(mensaje).upper().strip()  # Lee, convierte a mayúscula y limpia espacios
                if opcion in opciones_validas:  # Verifica si opción es válida
                    return opcion  # Retorna opción válida
                else:  # Si no es válida
                    print(f"❌ Opción no válida. Elija entre: {', '.join(opciones_validas)}")  # Mensaje error
            except EOFError:  #Se lanza cuando se alcanza inesperadamente el fin de un archivo o entrada (EOF = End Of File).
                print("\n❌ Entrada interrumpida")  # Mensaje de error
                return 'S'  # Retorna opción de salir
    
    @staticmethod  # Método estático
    def mostrar_llamada_turno(turno):  # Muestra mensaje de llamada
        """Muestra el mensaje de llamada de turno"""
        print("\n" + "🔔" * 20)  # Línea de campanas
        print(f"   LLAMANDO TURNO: {turno.numero}")  # Número de turno
        print(f"   Área: {turno.area}")  # Área del turno
        print("   Por favor, pase a la ventanilla")  # Instrucción
        print("🔔" * 20 + "\n")  # Línea de cierre
    
    @staticmethod  # Método estático
    def mostrar_despedida():  # Muestra mensaje de despedida
        """Muestra el mensaje de despedida"""
        print("\n✅ Gracias por su visita. ¡Hasta pronto!")  # Mensaje de salida

