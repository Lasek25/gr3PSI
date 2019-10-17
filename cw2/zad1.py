def fun(a_lista, b_lista):
    return a_lista[1::2]+b_lista[0::2]


lista_ab = fun([12, 14, 11, 17, 22], [8, 4, 1, 2, 9])
print(lista_ab)