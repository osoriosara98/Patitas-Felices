import random
from modelos.historia_clinica import HistoriaClinica
from data.db import historias_clinicas, pacientes, citas_registradas

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

def generar_id_unico_historia():
    while True:
        nuevo_id = str(random.randint(10000, 99999))
        if not any(h.id == nuevo_id for h in historias_clinicas):
            return nuevo_id

def crear_historia_clinica():
    print("\n--- Crear Historia Clínica ---")
    
    # Mostrar pacientes disponibles
    if not pacientes:
        print("❌ No hay pacientes registrados.")
        return
    
    print("Pacientes registrados:")
    for id_p, paciente in pacientes.items():
        print(f"ID: {id_p} - {paciente.nombre} ({paciente.especie})")
    
    id_paciente = input("Ingrese el ID del paciente: ")
    
    if id_paciente not in pacientes:
        print("❌ No existe un paciente con ese ID.")
        return
    
    paciente = pacientes[id_paciente]
    print(f"Paciente seleccionado: {paciente.nombre}")
    
    diagnostico = input("Diagnóstico: ")
    tratamiento = input("Tratamiento: ")
    vacunas = input("Vacunas aplicadas (opcional): ")
    observaciones = input("Observaciones adicionales (opcional): ")
    
    id_historia = generar_id_unico_historia()
    historia = HistoriaClinica(id_historia, id_paciente, diagnostico, tratamiento, vacunas, observaciones)
    historias_clinicas.append(historia)
    
    print(f"✅ Historia clínica creada exitosamente con ID: {id_historia}")
    
    # Auto-guardar datos
    auto_guardar_datos()

def buscar_paciente():
    print("Buscar paciente por:")
    print("1. ID del paciente")
    print("2. Nombre del paciente")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        id_paciente = input("Ingrese el ID del paciente: ")
        if id_paciente in pacientes:
            return pacientes[id_paciente]
        else:
            print("❌ No existe un paciente con ese ID.")
            return None
    elif opcion == "2":
        nombre_buscar = input("Ingrese el nombre del paciente: ").lower()
        for paciente in pacientes.values():
            if nombre_buscar in paciente.nombre.lower():
                return paciente
        print("❌ No se encontró un paciente con ese nombre.")
        return None
    else:
        print("❌ Opción inválida.")
        return None

def consultar_historial_paciente():
    print("\n--- Consultar Historial de Paciente ---")
    
    if not pacientes:
        print("❌ No hay pacientes registrados.")
        return
    
    paciente_encontrado = buscar_paciente()
    if not paciente_encontrado:
        return
    
    print(f"\n📋 Historial clínico de: {paciente_encontrado.nombre}")
    print(f"Especie: {paciente_encontrado.especie}, Raza: {paciente_encontrado.raza}")
    print("="*60)
    
    # Buscar historias clínicas del paciente
    historias_paciente = [h for h in historias_clinicas if h.id_paciente == paciente_encontrado.id]
    
    if not historias_paciente:
        print("📭 Este paciente no tiene historias clínicas registradas.")
        return
    
    # Ordenar por fecha (más reciente primero)
    historias_paciente.sort(key=lambda x: x.fecha_actualizacion, reverse=True)
    
    for historia in historias_paciente:
        print(historia)
    
    pausa_para_continuar()

def registrar_atencion_medica():
    print("\n--- Registrar Atención Médica ---")
    
    # Mostrar citas realizadas o por realizar
    if not citas_registradas:
        print("❌ No hay citas registradas.")
        return
    
    print("Citas disponibles para registrar atención:")
    citas_disponibles = [c for c in citas_registradas if c.estado in ["agendada", "realizada"]]
    
    if not citas_disponibles:
        print("❌ No hay citas disponibles para registrar atención.")
        return
    
    for i, cita in enumerate(citas_disponibles, 1):
        paciente = pacientes.get(cita.id_paciente)
        paciente_nombre = paciente.nombre if paciente else "Paciente no encontrado"
        print(f"{i}. Cita ID: {cita.id} - {paciente_nombre} - {cita.fecha} {cita.hora} - Estado: {cita.estado}")
    
    try:
        seleccion = int(input("Seleccione el número de la cita: ")) - 1
        if 0 <= seleccion < len(citas_disponibles):
            cita_seleccionada = citas_disponibles[seleccion]
        else:
            print("❌ Selección fuera de rango.")
            return
    except ValueError:
        print("❌ Entrada no válida.")
        return
    
    # Marcar cita como realizada
    cita_seleccionada.estado = "realizada"
    
    # Crear historia clínica
    print(f"\nRegistrando atención para la cita ID: {cita_seleccionada.id}")
    paciente = pacientes[cita_seleccionada.id_paciente]
    print(f"Paciente: {paciente.nombre}")
    print(f"Motivo de la consulta: {cita_seleccionada.motivo}")
    
    diagnostico = input("Diagnóstico: ")
    tratamiento = input("Tratamiento prescrito: ")
    vacunas = input("Vacunas aplicadas (opcional): ")
    observaciones = input("Observaciones adicionales (opcional): ")
    
    id_historia = generar_id_unico_historia()
    historia = HistoriaClinica(id_historia, cita_seleccionada.id_paciente, diagnostico, tratamiento, vacunas, observaciones)
    historias_clinicas.append(historia)
    
    print("✅ Atención médica registrada exitosamente.")
    print(f"📋 Historia clínica creada con ID: {id_historia}")
    
    # Auto-guardar datos
    auto_guardar_datos()
    print("📅 Cita marcada como realizada.")