from Monitor import Monitor
from Raton import Raton
from Teclado import Teclado


class Computadora:
    contador = 0

    def __init__(self,nombre, monitor, teclado, raton):
        Computadora.contador += 1
        self.__idComputadora = Computadora.contador
        self.__nombre = nombre
        self.__monitor = monitor
        self.__teclado = teclado
        self.__raton = raton

    @property
    def idComputadora(self):
        return self.__idComputadora

    @idComputadora.setter
    def idComputadora(self,idComputadora):
        self.__idComputadora = idComputadora

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def teclado(self):
        return self.__teclado
    @teclado.setter
    def teclado(self, teclado):
        self.__teclado = teclado

    @property
    def monitor(self):
        return self.__monitor
    @monitor.setter
    def monitor(self, monitor):
        self.__monitor = monitor

    @property
    def raton(self):
        return self.__raton
    @raton.setter
    def raton(self, raton):
        self.__raton = raton

    def __str__(self):
        return f'''
        {self.__nombre} : ID:{self.__idComputadora} 
        Monitor: {self.__monitor} 
        Teclado: {self.__teclado} 
        Raton: {self.__raton}
        '''

if __name__ == '__main__':

    teclado1 = Teclado('USB', 'Hp')
    raton1 = Raton('USB', 'HP')
    monitor1 = Monitor('HP', 15)
    computadora1 = Computadora('Hp', monitor1, teclado1, raton1)
    print(computadora1)