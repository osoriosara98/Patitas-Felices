"""
Utilidades para manejo de consola y interfaz de usuario
"""

# Constantes de mensajes
MENU_VOLVER_PRINCIPAL = "0. Volver al menú principal"
PROMPT_SELECCIONE_OPCION = "Seleccione una opción: "
MSG_OPCION_INVALIDA = "❌ Opción inválida. Intente de nuevo."
MSG_ENTRADA_NO_VALIDA = "⚠️ Entrada no válida. Ingrese un número."

def pausa_para_continuar(mensaje="Presione Enter para continuar..."):
    """Pausa la ejecución hasta que el usuario presione Enter"""
    input(f"\n{mensaje}")

def mostrar_titulo(titulo, ancho=60):
    """Muestra un título centrado con separadores"""
    print("\n" + "="*ancho)
    print(f"🐾 {titulo} 🐾".center(ancho))
    print("="*ancho)

def mostrar_seccion(titulo):
    """Muestra una sección dentro del menú"""
    print(f"\n{titulo}")

def mostrar_mensaje_exito(mensaje):
    """Muestra un mensaje de éxito"""
    print(f"✅ {mensaje}")

def mostrar_mensaje_error(mensaje):
    """Muestra un mensaje de error"""
    print(f"❌ {mensaje}")

def mostrar_mensaje_info(mensaje):
    """Muestra un mensaje informativo"""
    print(f"ℹ️ {mensaje}")

def mostrar_mensaje_alerta(mensaje):
    """Muestra un mensaje de alerta"""
    print(f"⚠️ {mensaje}")

def solicitar_entrada(prompt, requerido=True):
    """Solicita entrada del usuario con validación básica"""
    while True:
        entrada = input(prompt).strip()
        if entrada or not requerido:
            return entrada
        print("⚠️ Este campo es requerido.")

def solicitar_numero(prompt, minimo=None, maximo=None):
    """Solicita un número del usuario con validación"""
    while True:
        try:
            numero = int(input(prompt))
            if minimo is not None and numero < minimo:
                print(f"⚠️ El número debe ser mayor o igual a {minimo}")
                continue
            if maximo is not None and numero > maximo:
                print(f"⚠️ El número debe ser menor o igual a {maximo}")
                continue
            return numero
        except ValueError:
            print(MSG_ENTRADA_NO_VALIDA)

def confirmar_accion(mensaje="¿Está seguro?"):
    """Solicita confirmación del usuario"""
    respuesta = input(f"{mensaje} (s/n): ").lower()
    return respuesta in ['s', 'si', 'sí', 'y', 'yes']
