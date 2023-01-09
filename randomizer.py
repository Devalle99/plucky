import random
def pickScale():
    # define cada escala y selecciona una al azar
    jonico = 'zxcvbnm,'
    pentMin = 'zdvbj,'
    scales = [['Jónico', jonico], ['Pentatónica menor', pentMin]]
    randScales = random.choice(scales)
    # devuelve lista que contiene [strNombreDeEscala y lista[strSecuenciaLetras]]
    return randScales
# print(pickScale())

tableInit = {
    'z' : 'z',
    's' : 's',
    'x' : 'x',
    'd' : 'd',
    'c' : 'c',
    'v' : 'v',
    'g' : 'g',
    'b' : 'b',
    'h' : 'h',
    'n' : 'n',
    'j' : 'j',
    'm' : 'm',
    ',' : ','
}

def pickOrden(table):
    # shuffledTable = dict(zip(table.keys(), random.sample(table.values(), len(table))))
    keys = table.keys()
    values = table.values()
    random.shuffle(values)
    dict(zip(keys, values))
    print(table)

pickOrden(tableInit)



