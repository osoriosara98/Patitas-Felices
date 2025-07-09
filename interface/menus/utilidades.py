"""
Menú de utilidades y reportes avanzados
"""

from utils.consola import (
    mostrar_titulo, mostrar_seccion, pausa_para_continuar,
    PROMPT_SELECCIONE_OPCION, MSG_OPCION_INVALIDA
)
from data.utilidades import (
    generar_reporte_personalizado, buscar_por_criterio, obtener_citas_por_fecha,
    obtener_medicamentos_por_vencer, calcular_edad_promedio_pacientes,
    obtener_razas_mas_comunes, obtener_propietarios_activos
)
from data.db import propietarios, pacientes

def submenu_utilidades():
    """Menú de utilidades y reportes avanzados"""
    while True:
        print("\n🔧 UTILIDADES Y REPORTES AVANZADOS")
        print("="*50)
        mostrar_seccion("📊 REPORTES PERSONALIZADOS")
        print("1. Reporte general del sistema")
        print("2. Inventario crítico")
        print("3. Actividad de veterinarios")
        print("4. Pacientes más activos")
        print("5. Estadísticas por especies")
        
        mostrar_seccion("🔍 BÚSQUEDAS Y CONSULTAS")
        print("6. Buscar por criterio")
        print("7. Citas por rango de fechas")
        print("8. Medicamentos próximos a vencer")
        print("9. Propietarios activos")
        
        mostrar_seccion("📈 ESTADÍSTICAS")
        print("10. Edad promedio de pacientes")
        print("11. Razas más comunes")
        
        print("\n0. Volver al menú principal")
        print("="*50)
        
        opcion = input(PROMPT_SELECCIONE_OPCION)
        
        if opcion == "1":
            mostrar_reporte_personalizado("resumen_general")
        elif opcion == "2":
            mostrar_reporte_personalizado("inventario_critico")
        elif opcion == "3":
            mostrar_reporte_personalizado("actividad_veterinarios")
        elif opcion == "4":
            mostrar_reporte_personalizado("pacientes_activos")
        elif opcion == "5":
            mostrar_reporte_personalizado("estadisticas_especies")
        elif opcion == "6":
            realizar_busqueda_criterio()
        elif opcion == "7":
            consultar_citas_por_fecha()
        elif opcion == "8":
            mostrar_medicamentos_por_vencer()
        elif opcion == "9":
            mostrar_propietarios_activos()
        elif opcion == "10":
            mostrar_edad_promedio()
        elif opcion == "11":
            mostrar_razas_comunes()
        elif opcion == "0":
            break
        else:
            print(MSG_OPCION_INVALIDA)

def mostrar_reporte_personalizado(tipo_reporte):
    """Mostrar un reporte personalizado"""
    print("\n🔄 Generando reporte...")
    reporte = generar_reporte_personalizado(tipo_reporte)
    print(reporte)
    pausa_para_continuar()

def realizar_busqueda_criterio():
    """Realizar búsqueda por criterio específico"""
    print("\n🔍 BÚSQUEDA POR CRITERIO")
    print("="*30)
    print("Entidades disponibles:")
    print("1. Propietarios")
    print("2. Pacientes") 
    print("3. Citas")
    print("4. Medicamentos")
    
    entidades_map = {
        "1": "propietarios",
        "2": "pacientes", 
        "3": "citas",
        "4": "medicamentos"
    }
    
    seleccion = input("Seleccione entidad (1-4): ")
    if seleccion not in entidades_map:
        print("❌ Selección inválida.")
        pausa_para_continuar()
        return
    
    entidad = entidades_map[seleccion]
    campo = input("Ingrese el campo a buscar (ej: nombre, especie, fecha): ")
    valor = input("Ingrese el valor a buscar: ")
    
    resultados = buscar_por_criterio(entidad, campo, valor)
    
    if not resultados:
        print(f"❌ No se encontraron resultados para '{valor}' en el campo '{campo}'.")
    else:
        print(f"\n✅ Se encontraron {len(resultados)} resultado(s):")
        for resultado in resultados:
            print(f"• {resultado}")
    
    pausa_para_continuar()

def consultar_citas_por_fecha():
    """Consultar citas por rango de fechas"""
    print("\n📅 CONSULTAR CITAS POR FECHA")
    print("="*35)
    
    fecha_inicio = input("Fecha inicio (YYYY-MM-DD): ")
    fecha_fin = input("Fecha fin (YYYY-MM-DD, Enter para misma fecha): ")
    
    if not fecha_fin:
        fecha_fin = fecha_inicio
    
    citas = obtener_citas_por_fecha(fecha_inicio, fecha_fin)
    
    if not citas:
        print(f"❌ No se encontraron citas entre {fecha_inicio} y {fecha_fin}.")
    else:
        print(f"\n✅ Se encontraron {len(citas)} cita(s):")
        for cita in citas:
            paciente = pacientes.get(cita.id_paciente)
            paciente_nombre = paciente.nombre if paciente else "Paciente no encontrado"
            print(f"• {cita.fecha} {cita.hora} - {paciente_nombre} - {cita.motivo} - {cita.estado}")
    
    pausa_para_continuar()

def mostrar_medicamentos_por_vencer():
    """Mostrar medicamentos próximos a vencer"""
    print("\n💊 MEDICAMENTOS PRÓXIMOS A VENCER")
    print("="*40)
    
    try:
        dias = int(input("Días a futuro (Enter para 30): ") or "30")
    except ValueError:
        dias = 30
    
    medicamentos_vencen = obtener_medicamentos_por_vencer(dias)
    
    if not medicamentos_vencen:
        print(f"✅ No hay medicamentos que venzan en los próximos {dias} días.")
    else:
        print(f"⚠️ Se encontraron {len(medicamentos_vencen)} medicamento(s) próximos a vencer:")
        for med in medicamentos_vencen:
            print(f"• {med.nombre} - Vence: {med.fecha_vencimiento} - Stock: {med.stock}")
    
    pausa_para_continuar()

def mostrar_propietarios_activos():
    """Mostrar propietarios con actividad reciente"""
    print("\n👥 PROPIETARIOS ACTIVOS (últimos 90 días)")
    print("="*45)
    
    ids_activos = obtener_propietarios_activos()
    
    if not ids_activos:
        print("❌ No se encontraron propietarios con actividad reciente.")
    else:
        print(f"✅ Se encontraron {len(ids_activos)} propietario(s) activo(s):")
        for id_prop in ids_activos:
            if id_prop in propietarios:
                prop = propietarios[id_prop]
                print(f"• {prop.nombre} - Tel: {prop.telefono} - Email: {prop.correo}")
    
    pausa_para_continuar()

def mostrar_edad_promedio():
    """Mostrar edad promedio de pacientes"""
    print("\n📊 ESTADÍSTICAS DE EDAD")
    print("="*25)
    
    edad_promedio = calcular_edad_promedio_pacientes()
    total_pacientes = len(pacientes)
    
    if total_pacientes == 0:
        print("❌ No hay pacientes registrados.")
    else:
        print(f"📈 Edad promedio de pacientes: {edad_promedio:.1f} años")
        print(f"📊 Total de pacientes: {total_pacientes}")
        
        # Mostrar distribución por rangos de edad
        rangos = {"0-2": 0, "3-7": 0, "8-12": 0, "13+": 0}
        for pac in pacientes.values():
            edad = int(pac.edad)
            if edad <= 2:
                rangos["0-2"] += 1
            elif edad <= 7:
                rangos["3-7"] += 1
            elif edad <= 12:
                rangos["8-12"] += 1
            else:
                rangos["13+"] += 1
        
        print("\n📊 Distribución por rangos de edad:")
        for rango, cantidad in rangos.items():
            porcentaje = (cantidad / total_pacientes) * 100
            print(f"• {rango} años: {cantidad} pacientes ({porcentaje:.1f}%)")
    
    pausa_para_continuar()

def mostrar_razas_comunes():
    """Mostrar razas más comunes por especie"""
    print("\n🐕🐱 RAZAS MÁS COMUNES")
    print("="*25)
    
    print("1. Todas las especies")
    print("2. Solo perros")
    print("3. Solo gatos")
    print("4. Otra especie")
    
    opcion = input("Seleccione opción (1-4): ")
    
    especie = None
    if opcion == "2":
        especie = "Perro"
    elif opcion == "3":
        especie = "Gato"
    elif opcion == "4":
        especie = input("Ingrese la especie: ")
    
    razas = obtener_razas_mas_comunes(especie)
    
    if not razas:
        mensaje = f"para la especie '{especie}'" if especie else ""
        print(f"❌ No se encontraron razas {mensaje}.")
    else:
        titulo = f"para {especie}s" if especie else ""
        print(f"\n📊 Razas más comunes {titulo}:")
        for i, (raza, cantidad) in enumerate(razas[:10], 1):
            print(f"{i}. {raza}: {cantidad} paciente(s)")
    
    pausa_para_continuar()
