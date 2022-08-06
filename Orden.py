class Orden:
    contador = 0

    def __init__(self, computadoras):
        Orden.contador += 1
        self.__idOrden = Orden.contador
        self.__computadoras = computadoras

    @property
    def idOrden(self):
        return self.__idOrden

    @idOrden.setter
    def idOrden(self, idOrden):
        self.__idOrden = idOrden

    @property
    def computadoras(self):
        return self.__computadoras

    @computadoras.setter
    def idOrden(self, computadoras):
        self.__computadoras = computadoras

    def agregarComputadora(self, computadora):
        self.__computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ''
        for computadora in self.__computadoras:
            computadoras_str += computadora.__str__()

        return f'''
        Orden: {self.__idOrden} 
        Compra: {computadoras_str}
        '''

if __name__ == '__main__':
    computadoras = ['Lenovo', 'Acer', 'Hawei', 'Mac']
    computadora1 = Orden(computadoras)
    print(computadora1)
