# Based on the code numero_letra by efrenfuentes
# On: https://gist.github.com/efrenfuentes/3785655

CURRENCY = 'PESO_MEXICANO'

import json

currencyObj = json.load(open("./tools/currency.json"))
numeros = json.load(open("./tools/numeros.json"))

monedaInfo = currencyObj[CURRENCY]

def divideList(l, size):
    for i in range(0, len(l), size):
        yield l[i:i + size]

def separateNumber(number):
    nNumber = list(str(number)[::-1])
    if len(nNumber)>8:
        raise OverflowError()

    return list(divideList(nNumber, 3))
    
def getDecenasStr(number, money = True):
    if money:
        if (number[1] == '0') and (number[0] == '0'):                               # 0
            return ''
        elif ((number[1] == '0') and (number[0] != '0')) or (number[1] == '1'):     # 1-19
            num = int(number[1]+number[0])
            return numeros['UNIDADES'][num]
        elif (number[1] == '2') and (number[0] == '0'):                             # 20
            return numeros['DECENAS'][1]
        elif (number[1] == '2') and (number[0] != '0'):                             # 21-29
            num = int(number[0])
            return numeros['DECENAS'][2] + numeros['UNIDADES'][num]
        else:
            decenas = int(number[1])
            unidades = int(number[0])

            if number[0] == '0':                                                    # multiplo de 10
                return numeros['DECENAS'][decenas]
            else:                                                                   # resto de numeros
                return numeros['DECENAS'][decenas] + ' y ' + numeros['UNIDADES'][unidades]
    else: 
        if (number[1] == '0') and (number[0] == '0'):                               # 0
            return ''
        elif (number[1] == '0') and (number[0] == '1'):                             # 1                       # 1
            return numeros['UNIDADES'][20]
        elif ((number[1] == '0') and (number[0] != '0')) or (number[1] == '1'):     # 2-19
            num = int(number[1]+number[0])
            return numeros['UNIDADES'][num]
        elif (number[1] == '2') and (number[0] == '0'):                             # 20
            return numeros['DECENAS'][1]
        elif (number[1] == '2') and (number[0] == '1'):                             # 21
            return numeros['DECENAS'][2] + numeros['UNIDADES'][20]
        elif (number[1] == '2') and (number[0] != '0'):                             # 22-29
            num = int(number[0])
            return numeros['DECENAS'][2] + numeros['UNIDADES'][num]
        else:
            decenas = int(number[1])
            unidades = int(number[0])

            if number[0] == '0':                                                    # multiplo de 10
                return numeros['DECENAS'][decenas]
            if number[0] == '1':                                                    # escribir uno en lugar de un
                return numeros['DECENAS'][decenas] + ' y ' + numeros['UNIDADES'][20]
            else:                                                                   # resto de numeros
                return numeros['DECENAS'][decenas] + ' y ' + numeros['UNIDADES'][unidades]

def readTheeDigits(number, money = True):
    lNum = len(number)

    centenas = ''
    decenas = ''

    if lNum == 3:
        if (number[2] == '0') and (number[1] == '0') and (number[0] == '0'):    # 0
            return ''
        elif (number[2] == '1') and (number[1] == '0') and (number[0] == '0'):    # 100
            centenas = numeros['CENTENAS'][int(number[0])]
        else:
            centenas = numeros['CENTENAS'][int(number[2])]
            decenas = getDecenasStr(number, money)
    if lNum == 2:
        decenas = getDecenasStr(number, money)
    if lNum == 1:
        return getDecenasStr([number[0], '0'], money)   # Add 0 padding in tenths

    return centenas + ' ' + decenas

def writeNumber(number, money = True):
    nSeparated = separateNumber(number)
    level = len(nSeparated)
    sMillones = ''
    sMillares = ''
    sUnidades = ''

    if level == 3:  # Millones
        sMillones = readTheeDigits(nSeparated[2], money) + ' ' + numeros['SUPERIORES'][2]    # Varios millones
        sMillares = readTheeDigits(nSeparated[1], money) + ' ' + numeros['SUPERIORES'][0]    # Varios millares

        # Si es algun caso especial se va a re-escribir
        if (len(nSeparated[2]) == 1) and (nSeparated[2][0] == '1'):
            sMillones = readTheeDigits(nSeparated[2], money) + ' ' + numeros['SUPERIORES'][1]    # Un millon
        if (len(nSeparated[1]) == 3) and (nSeparated[1][2] == '0') and (nSeparated[1][1] == '0') and (nSeparated[1][0] == '1'):
            sMillares = numeros['SUPERIORES'][0]    # Mil
        if (len(nSeparated[1]) == 3) and (nSeparated[1][2] == '0') and (nSeparated[1][1] == '0') and (nSeparated[1][0] == '0'):
            sMillares = ''

    elif level == 2: # Millares
        sMillares = readTheeDigits(nSeparated[1], money) + ' ' + numeros['SUPERIORES'][0]    # Varios millares
        if (len(nSeparated[1]) == 1) and (nSeparated[1][0] == '1'):
            sMillares = numeros['SUPERIORES'][0]    # Mil
        
    sUnidades = readTheeDigits(nSeparated[0], money)    # Unidades normalitas

    if money:
        sNumero = (sMillones + ' ' + sMillares + ' ' + sUnidades).lstrip(' ')
        if len(sNumero) > 1:
            return (sMillones + ' ' + sMillares + ' ' + sUnidades).lstrip(' ') + ' ' + monedaInfo['NOMBRE_PLURAL']
        else:
            return (sMillones + ' ' + sMillares + ' ' + sUnidades).lstrip(' ') + ' ' + monedaInfo['NOMBRE_SINGULAR']
    else:
        return (sMillones + ' ' + sMillares + ' ' + sUnidades).lstrip(' ')

# def main():
#     print(writeNumber(1000, True))

# if __name__ == '__main__':
#     main()
