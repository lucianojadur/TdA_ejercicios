

class Heap():
	def __init__(self, l):
		self.__arr = l
		self.__n = len(l)
		self.__crearHeap__()

	def data(self):
		return self.__arr

	def vacio(self):
		return len(self.__arr) == 0

	def desacolar(self):
		dato = None
		if not self.vacio():
			dato = self.__arr[0]
			self.__arr[0], self.__arr[len(self.__arr)-1] = self.__arr[len(self.__arr)-1], self.__arr[0]	#swap
			self.__arr.pop()
		self.__heapify__(0)
		self.__n -= 1
		return dato

	def encolar(self, dato):
		self.__arr.append(dato)
		self.__n += 1
		self.__heapify__(self.__n-1)

	def data(self):
		return self.__arr

	def print(self):
		print(self.__arr)

	def __heapify__(self,i):
		lista = self.__arr
		mayor = i
		izq = 2*i + 1
		der = 2*i + 2

		if izq < len(lista) and lista[izq] > lista[mayor]:
			mayor = izq

		if der < len(lista) and lista[der] > lista[mayor]:
			mayor = der

		if mayor != i:
			lista[mayor], lista[i] = lista[i], lista[mayor]
			self.__heapify__(mayor)

	def __heapifyInsert__(self,i):
		padre = (i-1) / 2
		arr = self.__arr
		if arr[padre] > 0:
			if arr[i] > arr[padre]:
				arr[i], arr[padre] = arr[padre], arr[i]  
				__heapifyInsert__(padre)

	
	def __crearHeap__(self):
		arr = self.__arr
		for i in range(len(arr)//2 - 1, -1, -1):
			self.__heapify__(i)


###Fin de definicion de Heap