from logging import exception

from sqlalchemy import null


def ordenacao_binaria(lista, elemento, inicio, fim):
    meio = int((fim+inicio)/2)
    if(fim-inicio == 1):
        return null
    if(elemento == lista[meio]):
        return elemento
    if(elemento > lista[meio]):
        return ordenacao_binaria(lista, elemento, meio, fim)
    if(elemento < lista[meio]):
        return ordenacao_binaria(lista, elemento,inicio, meio)
lista = [11,22,33,44,55,66,77,88,99]
print("Elemento: ", ordenacao_binaria(lista, 22, 0, len(lista)))