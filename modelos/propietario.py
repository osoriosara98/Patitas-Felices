class Propietario:
    def __init__(self, id_propietario, nombre, telefono, correo, direccion):
        self.id = id_propietario
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.mascotas = []  # Lista de IDs de mascotas

    def __str__(self):
        return f"{self.nombre} (ID: {self.id}, Correo: {self.correo})"
