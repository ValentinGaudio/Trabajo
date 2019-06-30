#Esta funcion dice si el objeto es de tipo tupla o no
def es_tupla(objeto):
    if type(objeto) == tuple:
        return True
    else:
        return False
#Esta funcion convierte a todos en Billy!
def billies(lista):
    for i in range(0,len(lista)):
        lista[i] = 'Billy'
    return lista    
#Esta funcion dice si un numero es par o no
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

    
