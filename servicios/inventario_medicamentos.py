import random
from modelos.medicamento import Medicamento
from data.db import medicamentos

PAUSA_CONTINUAR = "\nPresione Enter para continuar..."

def pausa_para_continuar(mensaje="Presione Enter para continuar..."):
    """Pausa la ejecución hasta que el usuario presione Enter"""
    input(f"\n{mensaje}")

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

def generar_id_unico_medicamento():
    while True:
        nuevo_id = str(random.randint(100, 999))
        if nuevo_id not in medicamentos:
            return nuevo_id

def registrar_medicamento():
    print("\n--- Registro de Medicamento ---")
    nombre = input("Nombre del medicamento: ")
    descripcion = input("Descripción: ")
    
    while True:
        try:
            stock = int(input("Stock inicial: "))
            if stock > 0:
                break
            else:
                print("❌ El stock debe ser mayor a 0.")
        except ValueError:
            print("❌ Ingrese un número válido para el stock.")
    
    fecha_vencimiento = input("Fecha de vencimiento (YYYY-MM-DD): ")
    
    try:
        precio = float(input("Precio (opcional, presione Enter para 0): ") or "0")
    except ValueError:
        precio = 0.0

    id_medicamento = generar_id_unico_medicamento()
    medicamento = Medicamento(id_medicamento, nombre, descripcion, stock, fecha_vencimiento, precio)
    medicamentos[id_medicamento] = medicamento
    print(f"✅ Medicamento registrado con éxito. ID generado: {id_medicamento}")
    
    # Auto-guardar datos
    auto_guardar_datos()

def actualizar_stock():
    print("\n--- Actualizar Stock de Medicamento ---")
    mostrar_inventario()
    
    if not medicamentos:
        return
    
    id_medicamento = input("Ingrese el ID del medicamento: ")
    
    if id_medicamento not in medicamentos:
        print("❌ No existe un medicamento con ese ID.")
        return
    
    medicamento = medicamentos[id_medicamento]
    print(f"Medicamento seleccionado: {medicamento.nombre}")
    print(f"Stock actual: {medicamento.stock}")
    
    print("1. Entrada de stock (suma)")
    print("2. Salida de stock (resta)")
    opcion = input("Seleccione el tipo de movimiento: ")
    
    try:
        cantidad = int(input("Cantidad: "))
        if cantidad <= 0:
            print("❌ La cantidad debe ser mayor a 0.")
            return
    except ValueError:
        print("❌ Ingrese un número válido.")
        return
    
    motivo = input("Motivo del ajuste: ")
    
    if opcion == "1":
        medicamento.stock += cantidad
        print(f"✅ Stock actualizado. Nuevo stock: {medicamento.stock}")
    elif opcion == "2":
        if cantidad > medicamento.stock:
            print("❌ No hay suficiente stock disponible.")
            return
        medicamento.stock -= cantidad
        print(f"✅ Stock actualizado. Nuevo stock: {medicamento.stock}")
    else:
        print("❌ Opción inválida.")
        return
    
    print(f"📝 Motivo registrado: {motivo}")
    
    # Auto-guardar datos
    auto_guardar_datos()
    
    # Verificar alertas
    if medicamento.necesita_restock():
        print(f"⚠️ ALERTA: El medicamento {medicamento.nombre} necesita restock (Stock: {medicamento.stock})")

def mostrar_inventario():
    print("\n--- Inventario de Medicamentos ---")
    if not medicamentos:
        print("📭 No hay medicamentos registrados.")
        pausa_para_continuar()
        return
    
    for medicamento in medicamentos.values():
        print(f"ID: {medicamento.id} | {medicamento}")
        if medicamento.necesita_restock():
            print("   ⚠️ NECESITA RESTOCK")
        if medicamento.esta_por_vencer():
            print("   ⚠️ PRÓXIMO A VENCER")
    
    pausa_para_continuar()

def verificar_alertas_inventario():
    print("\n--- Alertas de Inventario ---")
    alertas_encontradas = False
    
    for medicamento in medicamentos.values():
        if medicamento.necesita_restock():
            print(f"🔴 STOCK BAJO: {medicamento.nombre} (Stock: {medicamento.stock})")
            alertas_encontradas = True
        
        if medicamento.esta_por_vencer():
            print(f"🟡 PRÓXIMO A VENCER: {medicamento.nombre} (Vence: {medicamento.fecha_vencimiento})")
            alertas_encontradas = True
    
    if not alertas_encontradas:
        print("✅ No hay alertas pendientes en el inventario.")
    
    pausa_para_continuar()