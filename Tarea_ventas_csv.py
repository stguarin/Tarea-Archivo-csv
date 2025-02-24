import pandas as pd 
df = pd.read_csv('C:\\Users\\Sarin\\Documents\\final\\\SalesJan2009.csv')

respuesta_usuario = int(input('si desea consultar las compras de un pais escriba 1\nsi desea consultar los metodos de pago usados en la ralizacion de una compra escrba 2 ? \n'))
if respuesta_usuario == 1:
    print('los siguientes pasies estan disponibles para la consulta de sus compras:') #bucle para mostrarlos paises disponibles a consultar
    for i in range (67):
        print(f'- {df.iloc[i,0]}')
    consulta = input('escriba el nombre del pais sobre el que desea consultar: ')
    resultado = str(df.loc[df['Paises']==consulta,'compras']) #busqueda del resultado del elemento deseado
    print(f'la cantidad de compras de {consulta} es de {resultado.split()[1]}') # impresion de el nombre del elemento
    #                                                                             y su correspondiente numero
if respuesta_usuario == 2:
    print('estos son los metodos de pago con los que a sido realizada una compra:')
    for i in range (67,73):
        print(f'- {df.iloc[i,0]}')
    consulta = input('escriba el nombre del metodo de pago sobre el que desea consultar: ')
    resultado = str(df.loc[df['Paises']==consulta,'compras'])
    print(f'la cantidad de compras con {consulta} es de {resultado.split()[1]}')
    