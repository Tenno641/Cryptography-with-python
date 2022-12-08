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


def enciphering(arr):
    ciphertext = []

    if len(arr) % 2 == 1:
        arr.append(0)

    times = len(arr)

    i = 0
    for x in range(0, int(times / 2)):
        ciphertext.append((arr[i] * key[0] + arr[i+1] * key[1]).__mod__(26))
        ciphertext.append((arr[i] * key[2] + arr[i+1] * key[3]).__mod__(26))
        i += 2

    matrix_to_text(ciphertext)


