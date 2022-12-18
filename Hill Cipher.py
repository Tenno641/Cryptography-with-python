#global uses
alphabet = ['a', 'b', 'c', 'd', 'e',
            'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q',
            'r', 's', 't', 'u', 'v', 'w',
            'x', 'y', 'z']

forbiddenDets = [2, 4, 6, 8, 10, 12, 13, 14, 16, 18, 20, 22, 24, 26]


#global functions
key = []
def key_to_matrix(text):

    for x in text:
        for y in alphabet:
            if x == y:
                key.append(alphabet.index(y))

lettersMatrix = []
def text_to_matrix(text):
    
    for x in text:
        for y in alphabet:
            if x == y:
                lettersMatrix.append(alphabet.index(y))


# - - - - - encrypting - - - - - 
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

    det = (invKey[0] * invKey[3] - invKey[1] * invKey[2]).__mod__(26)

    invDetKey = pow(det, -1, 26)

    #swapping
    invKey[0], invKey[3] = invKey[3], invKey[0]

    invKey[1] = 0 - invKey[1]
    invKey[2] = 0 - invKey[2]

    for x in range(0, int(len(invKey))):
        invKey[x] = invKey[x].__mod__(26)
        invKey[x] *= invDetKey
        newKey.append(invKey[x])

    deciphering(lettersMatrix, newKey)

# - - - - - decrypting - - - - - 
def deciphering(arr, deKey):
    ciphertext2 = []

    times = len(arr)

    i = 0
    for x in range(0, int(times / 2 )):
        ciphertext2.append((arr[i] * deKey[0] + arr[i+1] * deKey[1]).__mod__(26))
        ciphertext2.append((arr[i] * deKey[2] + arr[i+1] * deKey[3]).__mod__(26))
        i += 2

    matrix_to_text(ciphertext2)


#global function to convert matrix to text 
plaintext = ""
def matrix_to_text(arr2):
    global plaintext

    for x in arr2:
        plaintext = plaintext.__add__(alphabet[x])



#Key from the user
print("Enter 4 letters word as a key : ")
keyText = input().lower()

#checking the key validation 
if len(keyText) == 4:
    key_to_matrix(keyText)
else:
    print("Please, Enter 4 letters word!!")
    exit()

#checking the determinant validation 
det = (key[0] * key[3] - key[1] * key[2]).__mod__(26)
print(key)

if det <= 0:
    print(det, ": Negative number!, try another word.")
    exit()
    
while det > 26:
    det -= 26

print("determinant is : ", det)

if det in forbiddenDets:
    print(det, "is not invertible for the given modulus, try another word.")
    exit()

invDetKey = pow(det, -1, 26)


# UI
print("\nEnter Your choice\n1. Encrypt\n2. Decrypt\n3. Exit\n--------------------")

choice = input()

if choice == '1': # encryption

    print("Enter text to encrypt : ")
    message = input().lower()

    text_to_matrix(message)
    enciphering(lettersMatrix)
    print("text after encrypting : ", plaintext)

elif choice == '2': # decryption

    print("Enter text to decrypt : ")
    hiddenMessage = input().lower()

    text_to_matrix(hiddenMessage)
    inv_of_2x2_matrix(key)
    print("the original text : ", plaintext)

elif choice == '3':
    print("See Ya, Bye :(")
    exit()

else:
    print("Doesn't exist!")
