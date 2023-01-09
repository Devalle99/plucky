table = {
    'z' : 'z',
    's' : 'm',
    'x' : 'j',
    'd' : 'n',
    'c' : 'h',
    'v' : 'b',
    'g' : 'g',
    'b' : 'v',
    'h' : 'c',
    'n' : 'd',
    'j' : 'x',
    'm' : 's',
    ',' : ','
}

def convert(input):
    output = ''
    keyList = list(table.keys())
    for letra in input:
        for i in range(len(table)):
            if letra == table.get(keyList[i]):
                output = output + keyList[i]
    print(output)

convert('zmjnhbgvcdxs,')