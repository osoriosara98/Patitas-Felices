from data.db import pacientes, propietarios

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

def mostrar_datos_paciente(paciente):
    print(f"\nDatos actuales de {paciente.nombre}:")
    print(f"1. Nombre: {paciente.nombre}")
    print(f"2. Edad: {paciente.edad}")
    print(f"3. Especie: {paciente.especie}")
    print(f"4. Raza: {paciente.raza}")
    print(f"5. Peso: {paciente.peso}")
    print(f"6. Sexo: {paciente.sexo}")

def editar_campo_paciente(paciente, campo):
    campos = {
        "1": ("nombre", "Nombre"),
        "2": ("edad", "Edad"),
        "3": ("especie", "Especie"),
        "4": ("raza", "Raza"),
        "5": ("peso", "Peso"),
        "6": ("sexo", "Sexo"),
    }
    if campo in campos:
        attr, label = campos[campo]
        valor_actual = getattr(paciente, attr)
        nuevo_valor = input(f"Nuevo {label.lower()} (actual: {valor_actual}): ")
        if nuevo_valor.strip():
            setattr(paciente, attr, nuevo_valor)
            print(f"✅ {label} actualizado.")
        return True
    elif campo == "0":
        return False
    else:
        print("❌ Opción inválida.")
        return True

def editar_paciente():
    print("\n--- Editar Datos de Paciente ---")

    if not pacientes:
        print("❌ No hay pacientes registrados.")
        return

    print("Pacientes registrados:")
    for id_p, paciente in pacientes.items():
        print(f"ID: {id_p} - {paciente.nombre} ({paciente.especie})")

    id_paciente = input("Ingrese el ID del paciente a editar: ")

    if id_paciente not in pacientes:
        print("❌ No existe un paciente con ese ID.")
        return

    paciente = pacientes[id_paciente]
    mostrar_datos_paciente(paciente)

    while True:
        campo = input("\n¿Qué campo desea editar? (1-6, 0 para terminar): ")
        if campo == "0":
            break
        seguir = editar_campo_paciente(paciente, campo)
        if not seguir:
            break

    print(f"\n✅ Datos del paciente {paciente.nombre} actualizados correctamente.")
    
    # Auto-guardar datos
    auto_guardar_datos()

def mostrar_datos_propietario(propietario):
    print(f"\nDatos actuales de {propietario.nombre}:")
    print(f"1. Nombre: {propietario.nombre}")
    print(f"2. Teléfono: {propietario.telefono}")
    print(f"3. Correo: {propietario.correo}")
    print(f"4. Dirección: {propietario.direccion}")

def editar_campo_propietario(propietario, campo):
    campos = {
        "1": ("nombre", "Nombre"),
        "2": ("telefono", "Teléfono"),
        "3": ("correo", "Correo"),
        "4": ("direccion", "Dirección"),
    }
    if campo in campos:
        attr, label = campos[campo]
        valor_actual = getattr(propietario, attr)
        nuevo_valor = input(f"Nuevo {label.lower()} (actual: {valor_actual}): ")
        if nuevo_valor.strip():
            setattr(propietario, attr, nuevo_valor)
            print(f"✅ {label} actualizado.")
        return True
    elif campo == "0":
        return False
    else:
        print("❌ Opción inválida.")
        return True

def editar_propietario():
    print("\n--- Editar Datos de Propietario ---")

    if not propietarios:
        print("❌ No hay propietarios registrados.")
        return

    print("Propietarios registrados:")
    for id_p, propietario in propietarios.items():
        print(f"ID: {id_p} - {propietario.nombre}")

    id_propietario = input("Ingrese el ID del propietario a editar: ")

    if id_propietario not in propietarios:
        print("❌ No existe un propietario con ese ID.")
        return

    propietario = propietarios[id_propietario]
    mostrar_datos_propietario(propietario)

    while True:
        campo = input("\n¿Qué campo desea editar? (1-4, 0 para terminar): ")
        if campo == "0":
            break
        seguir = editar_campo_propietario(propietario, campo)
        if not seguir:
            break

    print(f"\n✅ Datos del propietario {propietario.nombre} actualizados correctamente.")
    
    # Auto-guardar datos
    auto_guardar_datos()

def menu_editar_datos():
    print("\n--- Menú de Edición ---")
    print("1. Editar datos de paciente")
    print("2. Editar datos de propietario")
    print("0. Volver al menú principal")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        editar_paciente()
    elif opcion == "2":
        editar_propietario()
    elif opcion == "0":
        return
    else:
        print("❌ Opción inválida.")