from datetime import datetime, timedelta
from data.db import citas_registradas, pacientes, propietarios, historias_clinicas
import xml.etree.ElementTree as ET

def pausa_para_continuar(mensaje="Presione Enter para continuar..."):
    """Pausa la ejecución hasta que el usuario presione Enter"""
    input(f"\n{mensaje}")

def generar_informe_mensual():
    print("\n--- Informe Mensual ---")
    año, mes = solicitar_anio_mes()
    if año is None or mes is None:
        return

    citas_mes = filtrar_citas_por_mes(año, mes)
    print(f"\n📊 INFORME MENSUAL - {mes:02d}/{año}")
    print("="*50)

    total_citas, citas_realizadas, citas_canceladas, citas_agendadas = calcular_estadisticas_generales(citas_mes)
    mostrar_estadisticas_generales(total_citas, citas_realizadas, citas_canceladas, citas_agendadas)

    pacientes_atendidos = obtener_pacientes_atendidos(citas_mes)
    print(f"🐾 Pacientes únicos atendidos: {len(pacientes_atendidos)}")

    mostrar_analisis_por_especie(pacientes_atendidos)
    mostrar_servicios_mas_solicitados(citas_mes)

    exportar = input("\n¿Desea exportar el informe a XML? (s/n): ").lower()
    if exportar == "s":
        exportar_informe_xml(año, mes, total_citas, citas_realizadas, citas_canceladas)
    
    pausa_para_continuar()

def solicitar_anio_mes():
    try:
        año = int(input("Ingrese el año (YYYY): "))
        mes = int(input("Ingrese el mes (1-12): "))
        if mes < 1 or mes > 12:
            print("❌ Mes inválido.")
            return None, None
        return año, mes
    except ValueError:
        print("❌ Formato de fecha inválido.")
        return None, None

def filtrar_citas_por_mes(año, mes):
    citas_mes = []
    for cita in citas_registradas:
        try:
            fecha_cita = datetime.strptime(cita.fecha, "%Y-%m-%d")
            if fecha_cita.year == año and fecha_cita.month == mes:
                citas_mes.append(cita)
        except ValueError:
            continue
    return citas_mes

def calcular_estadisticas_generales(citas_mes):
    total_citas = len(citas_mes)
    citas_realizadas = len([c for c in citas_mes if c.estado == "realizada"])
    citas_canceladas = len([c for c in citas_mes if c.estado == "cancelada"])
    citas_agendadas = len([c for c in citas_mes if c.estado == "agendada"])
    return total_citas, citas_realizadas, citas_canceladas, citas_agendadas

def mostrar_estadisticas_generales(total_citas, citas_realizadas, citas_canceladas, citas_agendadas):
    print(f"📅 Total de citas programadas: {total_citas}")
    print(f"✅ Citas realizadas: {citas_realizadas}")
    print(f"❌ Citas canceladas: {citas_canceladas}")
    print(f"⏳ Citas pendientes: {citas_agendadas}")
    if total_citas > 0:
        porcentaje_realizadas = (citas_realizadas / total_citas) * 100
        print(f"📈 Porcentaje de efectividad: {porcentaje_realizadas:.1f}%")

def obtener_pacientes_atendidos(citas_mes):
    return set(cita.id_paciente for cita in citas_mes if cita.estado == "realizada")

def mostrar_analisis_por_especie(pacientes_atendidos):
    especies = {}
    for id_paciente in pacientes_atendidos:
        if id_paciente in pacientes:
            especie = pacientes[id_paciente].especie
            especies[especie] = especies.get(especie, 0) + 1
    if especies:
        print("\n📊 Distribución por especie:")
        for especie, cantidad in especies.items():
            print(f"   {especie}: {cantidad} pacientes")

def mostrar_servicios_mas_solicitados(citas_mes):
    motivos = {}
    for cita in citas_mes:
        if cita.estado == "realizada":
            motivo = cita.motivo.lower()
            motivos[motivo] = motivos.get(motivo, 0) + 1
    if motivos:
        print("\n📋 Servicios más solicitados:")
        motivos_ordenados = sorted(motivos.items(), key=lambda x: x[1], reverse=True)
        for motivo, cantidad in motivos_ordenados[:5]:  # Top 5
            print(f"   {motivo.title()}: {cantidad} consultas")

def exportar_informe_xml(año, mes, total, realizadas, canceladas):
    """Exporta el informe a formato XML"""
    
    # Crear elemento raíz
    informe = ET.Element("InformeMensual")
    informe.set("año", str(año))
    informe.set("mes", str(mes))
    informe.set("fecha_generacion", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    
    # Estadísticas generales
    estadisticas = ET.SubElement(informe, "EstadisticasGenerales")
    ET.SubElement(estadisticas, "TotalCitas").text = str(total)
    ET.SubElement(estadisticas, "CitasRealizadas").text = str(realizadas)
    ET.SubElement(estadisticas, "CitasCanceladas").text = str(canceladas)
    
    if total > 0:
        porcentaje = (realizadas / total) * 100
        ET.SubElement(estadisticas, "PorcentajeEfectividad").text = f"{porcentaje:.1f}"
    
    # Escribir archivo
    tree = ET.ElementTree(informe)
    nombre_archivo = f"informe_{año}_{mes:02d}.xml"
    tree.write(nombre_archivo, encoding='utf-8', xml_declaration=True)
    
    print(f"✅ Informe exportado como '{nombre_archivo}'")

def generar_reporte_personalizado():
    print("\n--- Reporte Personalizado ---")
    print("1. Reporte por fechas")
    print("2. Reporte por especie")
    print("3. Reporte por veterinario")
    print("4. Reporte de pacientes más frecuentes")
    
    opcion = input("Seleccione el tipo de reporte: ")
    
    if opcion == "1":
        reporte_por_fechas()
    elif opcion == "2":
        reporte_por_especie()
    elif opcion == "3":
        reporte_por_veterinario()
    elif opcion == "4":
        reporte_pacientes_frecuentes()
    else:
        print("❌ Opción inválida.")

def reporte_por_fechas():
    print("\n--- Reporte por Fechas ---")
    fecha_inicio = input("Fecha de inicio (YYYY-MM-DD): ")
    fecha_fin = input("Fecha de fin (YYYY-MM-DD): ")
    
    try:
        inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
    except ValueError:
        print("❌ Formato de fecha inválido.")
        return
    
    citas_periodo = []
    for cita in citas_registradas:
        try:
            fecha_cita = datetime.strptime(cita.fecha, "%Y-%m-%d")
            if inicio <= fecha_cita <= fin:
                citas_periodo.append(cita)
        except ValueError:
            continue
    
    print(f"\n📊 Reporte del {fecha_inicio} al {fecha_fin}")
    print(f"Total de citas: {len(citas_periodo)}")
    
    for cita in citas_periodo:
        paciente = pacientes.get(cita.id_paciente)
        paciente_nombre = paciente.nombre if paciente else "Paciente no encontrado"
        print(f"• {cita.fecha} - {paciente_nombre} - {cita.motivo} - {cita.estado}")
    
    pausa_para_continuar()

def reporte_por_especie():
    print("\n--- Reporte por Especie ---")
    
    if not pacientes:
        print("❌ No hay pacientes registrados.")
        pausa_para_continuar()
        return
    
    especies_disponibles = set(p.especie for p in pacientes.values())
    print("Especies disponibles:", ", ".join(especies_disponibles))
    
    especie_buscar = input("Ingrese la especie: ").strip()
    
    pacientes_especie = [p for p in pacientes.values() if p.especie.lower() == especie_buscar.lower()]
    
    if not pacientes_especie:
        print(f"❌ No se encontraron pacientes de la especie '{especie_buscar}'.")
        pausa_para_continuar()
        return
    
    print(f"\n📊 Reporte de {especie_buscar}s:")
    print(f"Total de pacientes: {len(pacientes_especie)}")
    
    for paciente in pacientes_especie:
        citas_paciente = [c for c in citas_registradas if c.id_paciente == paciente.id]
        print(f"• {paciente.nombre} ({paciente.raza}) - {len(citas_paciente)} citas")
    
    pausa_para_continuar()

def reporte_por_veterinario():
    print("\n--- Reporte por Veterinario ---")
    
    # Cargar veterinarios del archivo
    try:
        with open("data/veterinarios.txt", "r", encoding="utf-8") as file:
            veterinarios = {}
            for linea in file:
                partes = linea.strip().split(",")
                if len(partes) >= 2:
                    veterinarios[partes[0]] = partes[1]
    except FileNotFoundError:
        print("❌ Archivo de veterinarios no encontrado.")
        pausa_para_continuar()
        return
    
    print("Veterinarios disponibles:")
    for id_vet, nombre in veterinarios.items():
        print(f"ID: {id_vet} - {nombre}")
    
    id_veterinario = input("Ingrese el ID del veterinario: ")
    
    if id_veterinario not in veterinarios:
        print("❌ Veterinario no encontrado.")
        pausa_para_continuar()
        return
    
    citas_veterinario = [c for c in citas_registradas if c.id_veterinario == id_veterinario]
    
    print(f"\n📊 Reporte del Dr. {veterinarios[id_veterinario]}:")
    print(f"Total de citas: {len(citas_veterinario)}")
    
    citas_realizadas = [c for c in citas_veterinario if c.estado == "realizada"]
    print(f"Citas realizadas: {len(citas_realizadas)}")
    
    for cita in citas_veterinario:
        paciente = pacientes.get(cita.id_paciente)
        paciente_nombre = paciente.nombre if paciente else "Paciente no encontrado"
        print(f"• {cita.fecha} - {paciente_nombre} - {cita.motivo} - {cita.estado}")
    
    pausa_para_continuar()

def reporte_pacientes_frecuentes():
    print("\n--- Reporte de Pacientes Más Frecuentes ---")
    
    # Contar citas por paciente
    conteo_pacientes = {}
    for cita in citas_registradas:
        if cita.estado == "realizada":
            conteo_pacientes[cita.id_paciente] = conteo_pacientes.get(cita.id_paciente, 0) + 1
    
    if not conteo_pacientes:
        print("❌ No hay pacientes con citas realizadas.")
        pausa_para_continuar()
        return
    
    # Ordenar por frecuencia
    pacientes_ordenados = sorted(conteo_pacientes.items(), key=lambda x: x[1], reverse=True)
    
    print("\n📊 Top 10 Pacientes Más Frecuentes:")
    for i, (id_paciente, cantidad) in enumerate(pacientes_ordenados[:10], 1):
        paciente = pacientes.get(id_paciente)
        if paciente:
            propietario = propietarios.get(paciente.id_propietario)
            propietario_nombre = propietario.nombre if propietario else "Propietario no encontrado"
            print(f"{i}. {paciente.nombre} ({paciente.especie}) - {cantidad} visitas - Dueño: {propietario_nombre}")
        else:
            print(f"{i}. Paciente ID {id_paciente} (no encontrado) - {cantidad} visitas")
    
    pausa_para_continuar()