alphabet = [' ', 'a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w',
            'x', 'y', 'z']


key = [3, 3, 2, 5]

lettersMatrix = []
def text_to_matrix(text):

    for x in text:
        for y in alphabet:
            if x == y:
                lettersMatrix.append(alphabet.index(y))


