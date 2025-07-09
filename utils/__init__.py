"""
Utilidades del sistema veterinario
"""

from .consola import (
    pausa_para_continuar,
    mostrar_titulo,
    mostrar_seccion,
    mostrar_mensaje_exito,
    mostrar_mensaje_error,
    mostrar_mensaje_info,
    mostrar_mensaje_alerta,
    solicitar_entrada,
    solicitar_numero,
    confirmar_accion,
    MENU_VOLVER_PRINCIPAL,
    PROMPT_SELECCIONE_OPCION,
    MSG_OPCION_INVALIDA,
    MSG_ENTRADA_NO_VALIDA
)

from .seleccion import (
    seleccionar_paciente,
    seleccionar_veterinario,
    cargar_veterinarios,
    seleccionar_opcion_menu
)
