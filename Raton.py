from DispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contador = 0

    def __init__(self, tipo, marca):
        Raton.contador += 1
        super().__init__(tipo, marca)
        self.__idRaton = Raton.contador

    @property
    def idRaton(self):
        return self.__idRaton

    @idRaton.setter
    def idRaton(self, idRaton):
        self.__idRaton = idRaton

    def __str__(self):
        return f'ID:{self.__idRaton} {super().__str__()}'


if __name__ == '__main__':
    raton1 = Raton('usb', 'lenovo')
    print(raton1)