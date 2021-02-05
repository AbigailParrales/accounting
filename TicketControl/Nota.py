import datetime
from tabulate import tabulate

from Venta import Venta
import tools.numeroConLetra as n2s

class Nota():
    def __init__(self, fecha = None, folio = None):
        if fecha:
            dateHolder = fecha.split("-")
            nYear = int(dateHolder[0])
            nMonth = int(dateHolder[1])
            nDay = int(dateHolder[2])
            self.fecha = datetime.date(nYear, nMonth, nDay)
        else:
            self.fecha = datetime.date.today()

        self.headers=["CANT", "DESCRIPCION", "P. UNIT", "IMPORTE"]

        self.ventas = []
        self.cantidades = [self.headers[0]]
        self.descripciones = [self.headers[1]]
        self.pUnitarios = [self.headers[2]]
        self.importes = [self.headers[3]]
        self.totalNota = 0
        self.folio = folio
        

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
        print('info: '+str(self.ventas))


        titulo = "NOTA DE VENTA\n\n"
        razonSocial = "MADERERIA TLALPUJAHUA\n"
        domicilio = "Periferico oriente No.3A\nCol. Jalisco, Tonala, Jal  C.P.45403\n"
        telefono = "\nTEL: 33 12 09 80 65\n"
        dia = self.fecha.strftime("%d/%m/%y")
        
        encabezado = titulo + razonSocial + domicilio + telefono + f"Fecha: {dia}\n==========================\n"
        # tablaArticulos = tabulate(self.ventas, self.headers,floatfmt=(None, None, '.2f', '.2f',)) + f"\n==========================\n"
        tablaArticulos = tabulate(self.ventas, self.headers,floatfmt='.2f') + f"\n==========================\n"
        total = "TOTAL: %.2f\n==========================\n"%(self.totalNota)
        totalConLetra = n2s.writeNumber(int(self.totalNota))
        decimales = str(round((self.totalNota%1)*100)) + '/100 M.N'

        notaStr = encabezado + tablaArticulos + total + totalConLetra + ' ' + decimales
        
        return notaStr