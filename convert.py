#tabla de ejemplo
# table = {
#     'z' : ',',
#     's' : 'm',
#     'x' : 'j',
#     'd' : 'n',
#     'c' : 'h',
#     'v' : 'b',
#     'g' : 'g',
#     'b' : 'v',
#     'h' : 'c',
#     'n' : 'd',
#     'j' : 'x',
#     'm' : 's',
#     ',' : 'z'
# }

table = {
    'z' : 'm',
    's' : ',',
    'x' : 'j',
    'd' : 'x',
    'c' : 'b',
    'v' : 'h',
    'g' : 's',
    'b' : 'z',
    'h' : 'c',
    'n' : 'd',
    'j' : 'n',
    'm' : 'g',
    ',' : 'v'
}

inv_table = {v: k for k, v in table.items()}

# entra str en desorden y sale en orden segun lo que dice 
# la tabla, lee value y devuelve key
def ordenar(input):
    output = ''
    keyList = list(table.keys())
    for letra in input:
        for i in range(len(table)):
            if letra == table.get(keyList[i]):
                output = output + keyList[i]
    return output

# entra str en orden y sale en desorden segun lo que dice 
# la tabla inversa, lee key y devuelve value
def desordenar(input):
    output = ''
    keyList = list(inv_table.keys())
    for letra in input:
        for i in range(len(inv_table)):
            if letra == inv_table.get(keyList[i]):
                output = output + keyList[i]
    return output

print(ordenar('m,j') + '\n' + desordenar(''))