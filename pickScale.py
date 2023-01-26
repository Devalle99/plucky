import random
def pickScale():
    lidio = 'zxcgbnm'
    jonico = 'zxcvbnm,'
    mixolidio = 'zxcvbnj'
    dorico = 'zxdvbnj,'
    eolico = 'zxdvbhj'
    frigio = 'zsdvbhj'
    locrio = 'zsdvghj'
    pentMin = 'zdvbj'
    scales = [['Lidio', lidio], ['Jónico', jonico], ['Mixolidio', mixolidio], ['Dórico', dorico], 
    ['Eólico', eolico], ['Frigio', frigio], ['Locrio', locrio], ['Pentatónica menor', pentMin]]
    randScales = random.choice(scales)
    return randScales
# print(pickScale())





