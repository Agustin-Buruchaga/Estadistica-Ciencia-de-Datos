import math

def media(lista):
	return sum(lista) / len(lista)

def mediana(lista):
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
        return "La lista est
        á vacía"
    
    # Calcular el rango
    valor_maximo = max(lista)
    valor_minimo = min(lista)
    rango = valor_maximo - valor_minimo
    
    return rango

def varianza(datos):    
    if len(datos) == 0:
        raise ValueError("La lista de datos no puede estar vacía.")
    promedio = media(datos)
    desviaciones = [(x - promedio) for x in datos]
    desviaciones_cuadraticas = [(d ** 2) for d in desviaciones]
    var = sum(desviaciones_cuadraticas) / len(datos)
    
    return var

def desviacion_estandar(datos):
    return varianza(datos)**0.5

def percentil(vals_in, q):
    #Eliminar valores NaNs (implementar a las demas funciones
    vals = []
    for v in vals_in:
        if math.isfinite(v):
            vals.append(v)
    #Ordenar lista
    vals.sort()
    #distancia entre el primer y ultimo elemento
    dist = len(vals)-1
    #calcular indice efectivo del percentil
    ieff = dist * q / 100
    #aislo la parte fraccional del indice efectivo
    fraction = ieff - int(ieff)
    #aislo la parte entera: corresponde al indice inferior
    i = int(ieff//1)
    #indice superior
    j = i + 1
    #hacer una interpolacion entre los valores correspondientes, a los indices encontrados
    percentil = vals[i] + (vals[j] - vals[i])*fraction
    return percentil

#rango intercuartilico
def iqr(vals_in):
    q1 = percentil(vals_in, 25)
    q3 = percentil(vals_in, 75)
    return q3 - q1
    