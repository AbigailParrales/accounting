class Venta():
    def __init__(self, cantidad, descripcion, pUnit):
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.pUnit = pUnit
        self.pTotalNum = float(self.cantidad) * float(self.pUnit)

    def __str__(self):
        return f"{self.cantidad}\t{self.descripcion}\t{self.pUnit}\t{self.pTotalNum}"

    def getVentaInfo(self):
        info = []
        info.append(self.cantidad)
        info.append(self.descripcion)
        info.append("%.2f"%(self.pUnit))
        info.append("%.2f"%(self.pTotalNum))
        return info

    def getImporteVenta(self):
        return self.pTotalNum