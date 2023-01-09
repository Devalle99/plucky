import random
orderedNotes = {
0 : 'sounds\do1Note.wav',
1 : 'sounds\diNote.wav',
2 : 'sounds\\reNote.wav',
3 : 'sounds\\riNote.wav',
4 : 'sounds\miNote.wav',
5 : 'sounds\\faNote.wav',
6 : 'sounds\\fiNote.wav',
7 : 'sounds\solNote.wav',
8 : 'sounds\siNote.wav',
9 : 'sounds\laNote.wav',
10 : 'sounds\liNote.wav',
11 : 'sounds\\tiNote.wav',
12 : 'sounds\do2Note.wav'
}

asociacion = {
0 : 0,
1 : 1,
2 : 2,
3 : 3,
4 : 4,
5 : 5,
6 : 6,
7 : 7,
8 : 8,
9 : 9,
10 : 10,
11 : 11,
12 : 12
}

# escalas son tuplas ya que tienen orden y son inmutables
jonico = (0, 2, 4, 5, 7, 9, 11, 12)
pentMin = (0, 3, 5, 7, 10, 12)
scales = [('Jónico', jonico), ('Pentatónica menor', pentMin)]
randScales = random.choice(scales)
print(randScales)

# randNotes = random.choices(orderedNotes, k=13)
# print(randNotes)

