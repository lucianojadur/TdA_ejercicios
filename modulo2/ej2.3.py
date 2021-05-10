from sys import argv
import csv


class Pedido():
	"""docstring for Pueblo"""
	def __init__(self, inicio, fin):
		self.__incio = int(inicio)
		self.__fin = int(fin)

	def init(self):
		return self.__incio

	def fin(self):
		return self.__fin

	def data(self):
		return self.__incio, self.fin



def inicio(pedido):
	return pedido.init()



def parse(path):
	pedidos = []

	with open(path) as File:
		register = csv.reader(File)
		for row in register:
			pedido = Pedido(int(row[0]), int(row[1]))
			pedidos.append(pedido)
	
	return pedidos



def sonCompatibles(pedidos, maximo):
	if maximo < len(pedidos):
		return True
		
	pedidos.sort(key=inicio)
	aceptados = []
	for pedido in pedidos:
		if len(aceptados) == maximo:
			for en_curso in aceptados:
				if en_curso.fin() < pedido.init():
					aceptados.remove(en_curso)
			if len(aceptados) == maximo:
				return False
		aceptados.append(pedido)
	
	return True


def main():
	"""	Se dispone de N máquinas para alquilar por una determinada cantidad de días a lo largo
		de un mes y se recibe una lista con M pedidos, indicando los días de inicio y fin del alquiler. 
	
		Diseñar un algoritmo que decida si es posible realizar o no todos los pedidos recibidos """

	assert len(argv) == 3
	disponibles = int(argv[2])
	pedidos = parse(argv[1])
	print("No problem" if sonCompatibles(pedidos, disponibles) else "No se pueden realizar")

main()