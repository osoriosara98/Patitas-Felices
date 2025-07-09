"""
Analizador de Backups - Sistema Veterinario Patitas Felices
"""

import json
import os
from datetime import datetime

def print_info_general(data):
    metadata = data.get('metadata', {})
    print(f"📅 Fecha de creación: {metadata.get('fecha_exportacion', 'No disponible')}")
    print(f"🔢 Versión: {metadata.get('version', 'No disponible')}")

def print_estadisticas_backup(data):
    print("\n📊 CONTENIDO DEL BACKUP:")
    print(f"👥 Propietarios: {len(data.get('propietarios', {}))}")
    print(f"🐾 Pacientes: {len(data.get('pacientes', {}))}")
    print(f"📅 Citas: {len(data.get('citas', []))}")
    print(f"💊 Medicamentos: {len(data.get('medicamentos', {}))}")
    print(f"📋 Historias clínicas: {len(data.get('historias_clinicas', []))}")

def analizar_propietarios(propietarios):
    if propietarios:
        print("\n👥 ANÁLISIS DE PROPIETARIOS:")
        mascotas_por_prop = [len(prop.get('mascotas', [])) for prop in propietarios.values()]
        print(f"   • Promedio de mascotas por propietario: {sum(mascotas_por_prop)/len(mascotas_por_prop):.1f}")
        print(f"   • Máximo de mascotas: {max(mascotas_por_prop)}")
        print(f"   • Mínimo de mascotas: {min(mascotas_por_prop)}")

def analizar_pacientes(pacientes):
    if pacientes:
        print("\n🐾 ANÁLISIS DE PACIENTES:")
        especies = {}
        razas = {}
        edades = []
        for pac in pacientes.values():
            especie = pac.get('especie', 'Desconocido')
            especies[especie] = especies.get(especie, 0) + 1
            raza = pac.get('raza', 'Desconocido')
            razas[raza] = razas.get(raza, 0) + 1
            try:
                edad = int(pac.get('edad', 0))
                edades.append(edad)
            except ValueError:
                pass
        print("   • Especies:")
        for esp, cant in especies.items():
            print(f"     - {esp}: {cant} pacientes")
        if edades:
            print(f"   • Edad promedio: {sum(edades)/len(edades):.1f} años")
            print(f"   • Rango de edades: {min(edades)}-{max(edades)} años")

def analizar_citas(citas):
    if citas:
        print("\n📅 ANÁLISIS DE CITAS:")
        estados = {}
        veterinarios = {}
        for cita in citas:
            estado = cita.get('estado', 'Desconocido')
            estados[estado] = estados.get(estado, 0) + 1
            vet = cita.get('id_veterinario', 'Desconocido')
            veterinarios[vet] = veterinarios.get(vet, 0) + 1
        print("   • Estados de citas:")
        for estado, cant in estados.items():
            print(f"     - {estado.capitalize()}: {cant}")
        print("   • Citas por veterinario:")
        for vet_id, cant in veterinarios.items():
            if vet_id == "1234":
                vet_nombre = "Dr. Juan Pérez"
            elif vet_id == "5678":
                vet_nombre = "Dra. María López"
            else:
                vet_nombre = f"ID {vet_id}"
            print(f"     - {vet_nombre}: {cant} citas")

def analizar_medicamentos(medicamentos):
    if medicamentos:
        print("\n💊 ANÁLISIS DE MEDICAMENTOS:")
        stock_bajo = 0
        stock_total = 0
        precios = []
        for med in medicamentos.values():
            try:
                stock = int(med.get('stock', 0))
                stock_total += stock
                if stock <= 10:
                    stock_bajo += 1
                precio = float(med.get('precio', 0))
                precios.append(precio)
            except (ValueError, TypeError):
                pass
        print(f"   • Medicamentos con stock bajo (≤10): {stock_bajo}")
        print(f"   • Stock total en inventario: {stock_total} unidades")
        if precios:
            print(f"   • Precio promedio: ${sum(precios)/len(precios):,.0f}")
            print(f"   • Valor total inventario: ${sum(precios):,.0f}")

def print_file_info(archivo_backup):
    tamano_kb = os.path.getsize(archivo_backup) / 1024
    print("\n📁 INFORMACIÓN DEL ARCHIVO:")
    print(f"   • Tamaño: {tamano_kb:.2f} KB")
    with open(archivo_backup, 'r') as f:
        print(f"   • Líneas totales: {len(f.readlines())}")

def analizar_backup(archivo_backup):
    """Analizar un archivo de backup y mostrar estadísticas detalladas"""

    if not os.path.exists(archivo_backup):
        print(f"❌ Archivo {archivo_backup} no encontrado")
        return

    try:
        with open(archivo_backup, 'r', encoding='utf-8') as f:
            data = json.load(f)

        print("🔍 ANÁLISIS DETALLADO DEL BACKUP")
        print("="*50)

        print_info_general(data)
        print_estadisticas_backup(data)
        analizar_propietarios(data.get('propietarios', {}))
        analizar_pacientes(data.get('pacientes', {}))
        analizar_citas(data.get('citas', []))
        analizar_medicamentos(data.get('medicamentos', {}))
        print_file_info(archivo_backup)

        print("="*50)
        print("✅ Análisis completado")

    except Exception as e:
        print(f"❌ Error al analizar backup: {e}")

def comparar_backups(archivo1, archivo2):
    """Comparar dos archivos de backup"""
    print("🔄 COMPARACIÓN DE BACKUPS")
    print("="*40)
    
    for archivo in [archivo1, archivo2]:
        if os.path.exists(archivo):
            with open(archivo, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            print(f"\n📁 {os.path.basename(archivo)}:")
            print(f"   Propietarios: {len(data.get('propietarios', {}))}")
            print(f"   Pacientes: {len(data.get('pacientes', {}))}")
            print(f"   Citas: {len(data.get('citas', []))}")
            print(f"   Medicamentos: {len(data.get('medicamentos', {}))}")
            print(f"   Historias: {len(data.get('historias_clinicas', []))}")
        else:
            print(f"❌ {archivo} no encontrado")

if __name__ == "__main__":
    # Analizar el backup seleccionado por el usuario
    backup_dir = "data/backups"
    if os.path.exists(backup_dir):
        archivos = [f for f in os.listdir(backup_dir) if f.endswith('.json')]
        if archivos:
            print("Backups disponibles:")
            for idx, nombre in enumerate(archivos, 1):
                print(f"  {idx}. {nombre}")
            try:
                opcion = int(input("Seleccione el número del backup a analizar: "))
                if 1 <= opcion <= len(archivos):
                    archivo_elegido = archivos[opcion - 1]
                    print(f"\n📁 Analizando backup: {archivo_elegido}")
                    analizar_backup(os.path.join(backup_dir, archivo_elegido))
                else:
                    print("❌ Opción no válida")
            except ValueError:
                print("❌ Entrada no válida")
        else:
            print("❌ No se encontraron archivos de backup")
    else:
        print("❌ Directorio de backups no encontrado")