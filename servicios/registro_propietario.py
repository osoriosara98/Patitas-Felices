from modelos.propietario import Propietario
from data.db import propietarios

def auto_guardar_datos():
    """Guarda automáticamente los datos de la sesión actual"""
    try:
        from data.db import guardar_sesion_actual
        
        archivo_guardado = guardar_sesion_actual()
        if archivo_guardado:
            nombre_archivo = archivo_guardado.split('\\')[-1] if '\\' in archivo_guardado else archivo_guardado.split('/')[-1]
            print(f"💾 Sesión actualizada: {nombre_archivo}")
        
    except Exception as e:
        print(f"⚠️ Error al actualizar sesión: {e}")

def registrar_propietario():
    print("\n--- Registro de Propietario ---")
    id_propietario = input("ID del Propietario: ")
    if id_propietario in propietarios:
        print("❌ Ya existe un propietario con ese ID.")
        return
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    correo = input("Correo electrónico: ")
    direccion = input("Dirección: ")

    propietario = Propietario(id_propietario, nombre, telefono, correo, direccion)
    propietarios[id_propietario] = propietario
    print("✅ Propietario registrado con éxito.")
    
    # Auto-guardar datos
    auto_guardar_datos()
