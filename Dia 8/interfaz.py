from gestor_turnos import GestorTurnos


class InterfazUsuario:
    """Maneja la interfaz de usuario y validación de entradas"""
    
    @staticmethod
    def mostrar_menu(areas_disponibles: dict):
        """Muestra el menú de opciones"""
        print("\n" + "=" * 40)
        print("  BIENVENIDO A FARMACIA PYTHON")
        print("=" * 40)
        print("\n📋 SACAR TURNO:")
        for codigo, nombre in areas_disponibles.items():
            print(f"[{codigo}] - {nombre}")
        
        print("\n🔔 LLAMAR TURNO:")
        print("[1] - Llamar turno de Perfumería")
        print("[2] - Llamar turno de Farmacia")
        print("[3] - Llamar turno de Cosmética")
        
        print("\n📊 INFORMACIÓN:")
        print("[T] - Ver turnos pendientes")
        print("[E] - Ver estadísticas")
        print("[S] - Salir")
        print("=" * 40)
    
    @staticmethod
    def solicitar_opcion(mensaje: str, opciones_validas: list) -> str:
        """Solicita una opción al usuario con validación"""
        while True:
            try:
                opcion = input(mensaje).upper().strip()
                if opcion in opciones_validas:
                    return opcion
                else:
                    print(f"❌ Opción no válida. Elija entre: {', '.join(opciones_validas)}")
            except EOFError:
                print("\n❌ Entrada interrumpida")
                return 'S'
    
    @staticmethod
    def mostrar_llamada_turno(turno):
        """Muestra el mensaje de llamada de turno"""
        print("\n" + "🔔" * 20)
        print(f"   LLAMANDO TURNO: {turno.numero}")
        print(f"   Área: {turno.area}")
        print("   Por favor, pase a la ventanilla")
        print("🔔" * 20 + "\n")
    
    @staticmethod
    def mostrar_despedida():
        """Muestra el mensaje de despedida"""
        print("\n✅ Gracias por su visita. ¡Hasta pronto!")
