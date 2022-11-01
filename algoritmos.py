import math 

def distancia_euclidiana(x_1, y_1, x_2, y_2):
    a = (x_2 - x_1)*(x_2 - x_1)
    b = (y_2 - y_1)*(y_2 - y_1)
    
    c = a + b
    
    distancia = math.sqrt(c)
    
    return distancia
    
	