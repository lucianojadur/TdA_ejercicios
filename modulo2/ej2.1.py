from sys import argv
import csv


class Pueblo():
	"""docstring for Pueblo"""
	def __init__(self, nombre, km):
		self.__nombre = nombre
		self.__km = int(km)

	def nombre(self):
		return self.__nombre

	def km(self):
		return self.__km

	def data(self):
		return self.__nombre, self.__km


def getKm(pueblo):
	return pueblo.km()



def parse(path):
	pueblos = []

	with open(path) as File:
		register = csv.reader(File)
		for row in register:
			pueblo = Pueblo(row[0], int(row[1]))
			pueblos.append(pueblo)
	
	return pueblos


def obtenerDistribucionPatrullas(pueblos):
	patrullas = []
	pueblos.sort(key=getKm)
	pivot = pueblos[0]

	for i in range(0, len(pueblos)):
		if i < len(pueblos) - 1:
			for j in range(i+1, len(pueblos)):
				if pueblos[j].km() > pivot.km() + 50:
					pivot = pueblos[j-1]
					for k in range(j, len(pueblos)):
						if pueblos[k].km() > pivot.km() + 50:
							patrullas.append(pivot)
							pivot = pueblos[k]
							i = k
							break
					break
		#si no pongo este if aparte, en caso de quedar un único pueblo aislado no lo agrega a patrullas
		if i+1 == len(pueblos) and pivot not in patrullas:	
			patrullas.append(pivot)

	return patrullas


def main():
	"""EJ:1 dada una lista de pueblos a los que se llega mediante la misma ruta y los kilómetros de la ruta
	en los cuales se abre una bifurcación hacia cada pueblo, diseñar un algoritmo que, usando una estrategia
	Greedy, obtenga la mínima cantidad de bifurcaciones en las cuales colocar una patrulla de forma tal que
	dentro de una distancia de +- 50 km no halla otra bifurcación con patrulla"""
	assert len(argv) == 2
	pueblos = parse(argv[1])
	patrullas = obtenerDistribucionPatrullas(pueblos)
	print([patrulla.data() for patrulla in patrullas])


main()