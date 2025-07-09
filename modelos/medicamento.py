from datetime import datetime

class Medicamento:
    def __init__(self, id_medicamento, nombre, descripcion, stock, fecha_vencimiento, precio=0.0):
        self.id = id_medicamento
        self.nombre = nombre
        self.descripcion = descripcion
        self.stock = stock
        self.fecha_vencimiento = fecha_vencimiento
        self.precio = precio
        self.stock_minimo = max(1, int(stock * 0.1))  # 10% del stock inicial

    def __str__(self):
        return (f"Medicamento: {self.nombre} (ID: {self.id}) - Stock: {self.stock}, "
                f"Vencimiento: {self.fecha_vencimiento}, Precio: ${self.precio}")

    def esta_por_vencer(self, dias_alerta=30):
        """Verifica si el medicamento está por vencer en los próximos días especificados"""
        try:
            fecha_venc = datetime.strptime(self.fecha_vencimiento, "%Y-%m-%d")
            dias_restantes = (fecha_venc - datetime.now()).days
            return dias_restantes <= dias_alerta
        except:
            return False
            raise

    def necesita_restock(self):
        """Verifica si el medicamento necesita restock (está al 10% o menos)"""
        return self.stock <= self.stock_minimo 