#Laboratorio Mundo PC
from Computadora import Computadora
from Monitor import Monitor
from Orden import Orden
from Raton import Raton
from Teclado import Teclado

#Objetos teclado
teclado1 = Teclado('USB', 'Hp')
teclado2 = Teclado('Bluetooth', 'Acer')

#Objetos raton
raton1 = Raton('USB', 'HP')
raton2 = Raton('Bluetooth', 'Acer')

#Objetos monitor
monitor1 = Monitor('HP', 15)
monitor2 = Monitor('Acer', 14)

#Objetos computadora
computadora1 = Computadora('Hp', monitor1, teclado1, raton1)
computadora2 = Computadora('Acer', monitor2, teclado2, raton2)
computadora3 = Computadora('Lenovo', monitor2, teclado1, raton2)

#Objetos de tipo orden
computadoras1 = [computadora1, computadora2]
computadoras2 = [computadora2,computadora3]
orden1 = Orden(computadoras1)
orden2 = Orden(computadoras2)
print(orden1)
print(orden2)
orden1.agregarComputadora(computadora3)
print(orden1)