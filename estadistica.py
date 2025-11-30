def media(lista):
	return sum(lista) / len(lista)

def mediana(archivo):
	lista_ordenada = sorted(lista)
	n = len(lista_ordenada)
	mitad = n // 2
	
	if n % 2 == 0:
		return(lista_ordenada[mitad - 1] + lista_ordenada[mitad]) / 2
	else:
		return lista_ordenada[mitad]

def moda(lista):
    frecuencias = {}

    # contar
    for valor in lista:
        if valor in frecuencias:
            frecuencias[valor] += 1
        else:
            frecuencias[valor] = 1

    # obtener frecuencia máxima
    f_max = 0
    for valor in frecuencias:
        if frecuencias[valor] > f_max:
            f_max = frecuencias[valor]

    # obtener todas las modas
    modas = []
    for valor in frecuencias:
        if frecuencias[valor] == f_max:
            modas.append(valor)

    return modas, f_max

def calcular_rango(lista):
    # Verificar si la lista no está vacía
    if not lista:
        return "La lista está vacía"
    
    # Calcular el rango
    valor_maximo = max(lista)
    valor_minimo = min(lista)
    rango = valor_maximo - valor_minimo
    
    return rango