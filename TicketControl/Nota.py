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

        self.headers=["Cantidad", "Descripcion", "Precio Unitario", "Importe"]

        self.ventas = []
        self.cantidades = [self.headers[0]]
        self.descripciones = [self.headers[1]]
        self.pUnitarios = [self.headers[2]]
        self.importes = [self.headers[3]]
        self.totalNota = 0
        

    def registrarVenta(self, cantidad, descripcion, pUnit):
        venta = Venta(cantidad, descripcion, pUnit)

        self.cantidades.append(cantidad)
        self.descripciones.append(descripcion)
        self.pUnitarios.append(pUnit)
        self.importes.append(venta.getImporteVenta())

        self.ventas.append(venta.getVentaInfo())

        self.totalNota = self.getTotalNota()
    
    def getCantidades(self):
        return self.cantidades

    def getDescripciones(self):
        return self.descripciones

    def getPUnitarios(self):
        return self.pUnitarios

    def getImportes(self):
        return self.importes

    def getTotalNota(self):
        if len(self.importes)>1:
            return sum(self.importes[1:])
    
    def __str__(self):
        return tabulate(self.ventas, self.headers)