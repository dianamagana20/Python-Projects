from DispositivoEntrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contador = 0

    def __init__(self, tipo, marca):
        Teclado.contador += 1
        super().__init__(tipo, marca)
        self.__idTeclado = Teclado.contador

    @property
    def idTeclado(self):
        return self.__idTeclado

    @idTeclado.setter
    def idTeclado(self, idTeclado):
        self.__idTeclado = idTeclado

    def __str__(self):
        return f'ID:{self.__idTeclado}, {super().__str__()}'


if __name__ == '__main__':
    teclado1 = Teclado('134','lenovo')
    print(teclado1)
