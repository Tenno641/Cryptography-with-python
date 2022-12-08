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


#making new key for deciphering


def inv_of_2x2_matrix(invKey):
    newKey = []

    invDetKey = 3

    #swapping
    invKey[0], invKey[3] = invKey[3], invKey[0]

    invKey[1] = 0 - invKey[1]
    invKey[2] = 0 - invKey[2]

    for x in range(0, int(len(invKey))):
        invKey[x] = invKey[x].__mod__(26)
        invKey[x] *= invDetKey
        newKey.append(invKey[x])

    deciphering(lettersMatrix, newKey)


def deciphering(arr, deKey):
    ciphertext2 = []

    if len(arr) % 2 == 1:
        arr.append(0)

    times = len(arr)

    i = 0
    for x in range(0, int(times / 2 )):
        ciphertext2.append((arr[i] * deKey[0] + arr[i+1] * deKey[1]).__mod__(26))
        ciphertext2.append((arr[i] * deKey[2] + arr[i+1] * deKey[3]).__mod__(26))
        i += 2

    matrix_to_text(ciphertext2)


plaintext = ""
def matrix_to_text(arr2):
    global plaintext

    for x in arr2:
        plaintext = plaintext.__add__(alphabet[x])
