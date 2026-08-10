datos = [4,9,2,15,7]
mayor = 9
posicion = 3

## Antes

print('Antes: ')
print(datos)
print(mayor)
print(posicion)


if datos[posicion] > mayor:
    mayor = datos[posicion]
posicion = posicion + 1

print('Despues: ')

print(datos)
print(mayor)
print(posicion)