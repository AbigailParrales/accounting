class Venta():
    def __init__(self, cantidad, descripcion, pUnit):
        self.cantidad = cantidad
        self.descripcion = descripcion
        self.pUnit = pUnit
        self.pTotalNum = self.cantidad * self.pUnit

    def __str__(self):
        return f"{self.cantidad}\t{self.descripcion}\t{self.pUnit}\t{self.pTotalNum}"

    def getVentaInfo(self):
        info = []
        info.append(self.cantidad)
        info.append(self.descripcion)
        info.append(self.pUnit)
        info.append(self.pTotalNum)
        return info