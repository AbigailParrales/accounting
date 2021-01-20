import datetime
from tabulate import tabulate

from Venta import Venta


class Nota():
    def __init__(self, fecha = None):
        if fecha:
            dateHolder = fecha.split("-")
            nYear = int(dateHolder[0])
            nMonth = int(dateHolder[1])
            nDay = int(dateHolder[2])
            self.fecha = datetime.date(nYear, nMonth, nDay)
        else:
            self.fecha = datetime.date.today()

        self.ventas = []
        self.total = 0

    def registrarVenta(self, cantidad, descripcion, pUnit):
        venta = Venta(cantidad, descripcion, pUnit)
        self.ventas.append(venta.getVentaInfo())

    def __str__(self):
        headers=["Cantidad", "Descripcion", "Precio Unitario", "Importe"]
        return tabulate(self.ventas, headers)