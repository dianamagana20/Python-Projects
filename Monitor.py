class Monitor():
    contador = 0

    def __init__(self, marca, tamanio):
        Monitor.contador += 1
        self.__marca = marca
        self.__idMonitor = Monitor.contador
        self.__tamanio = tamanio

    @property
    def idMonitor(self):
        return self.__idMonitor

    @idMonitor.setter
    def idTeclado(self, idMonitor):
        self.__idMonitor = idMonitor

    @property
    def marca(self):
        return self.__marca

    @idMonitor.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def tamanio(self):
        return self.__tamanio
    @tamanio.setter
    def tamanio(self, tamanio):
        self.__tamanio = tamanio

    def __str__(self):
        return f'ID:{self.__idMonitor}, Marca:{self.__marca}, Tamanio:{self.__tamanio} '

if __name__ == '__main__':
    monitor1 = Monitor('Lenovo', '15 in')
    print(monitor1)

