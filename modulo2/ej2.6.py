from sys import argv
from heap import *

class Pedido():
	def __init__(self, fin, peso):
		self.__t = fin
		self.__w = peso

	def t(self):
		return self.__t

	def W(self):
		return self.__w

	def data(self):
		return self.__t, self.__w

	def __gt__(self, other):
		return self.__t > other.__t

	def __lt__(self, other):
		return self.__t < other.__t

	def __eq__(self, other):
		return self.__t == other.__t

###Fin de definición de Pedido



def tiempoTotalMinimo(pedidos):
	"""Dada una lista de pedidos, donde cada pedido tiene un valor asociado que representa
	su importancia, que influye en la felicidad del cliente según cuánto tarde en ser realizado

	Diseñar un algoritmo que minimice la sumatoria de Ci*Wi, con:
		Ci: el instante en el cual termina de ejecutarse el pedido i,
		Wi: el peso asociado a la importancia del pedido i.
	"""

	# A mayor importancia, Ci * Wi será menor cuanto menor sea Ci
	# Conviene ejecutar primero los pedidos más demandados

	cola = Heap(pedidos)
#	print([pedido.data() for pedido in cola.data()])
	suma = 0
	C = 0
	for pedido in cola.data():
		C += pedido.t()
		suma += C * pedido.W()

	return suma 




def main():

	pedido2 = Pedido(3, 1)
	pedido1 = Pedido(8, 5)
	pedido3 = Pedido(4, 2)
	pedido5 = Pedido(5, 3)
	pedido4 = Pedido(7, 4)

	lista = []
	lista.append(pedido1)
	lista.append(pedido2)
	lista.append(pedido3)
	lista.append(pedido4)
	lista.append(pedido5)

	print("el tiempo total minimo es ", tiempoTotalMinimo(lista))

main()