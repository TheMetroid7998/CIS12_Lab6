
def alpha_line(header=' ', shift=0):
    """Prints a header letter and the alphabet with an offset, all separated by pipes."""
    print(f"| {header} ", end='|')
    for letter in range(65, 91):
        shifted_letter = (letter - 65 + shift) % 26 + 65
        print(f"| {chr(shifted_letter)} ", end='')
    print(f"|")

def header_line():
    """Prints a header and 26 columns of dashes, separated by pipes."""
    print(f"|---", end='|')
    for _ in range(26):
        print(f"|---", end='')
    print(f"|")

def vigenere_sq(header=' ', shift=0):
    """Prints an initial 27 columns with the alphabet, a header line of dashes, and 26 rows of the alphabet with increasing offsets."""
    alpha_line(' ')
    header_line()
    shift = 0
    for row in range(26):
        header = chr(row + 65)
        alpha_line(header, row)

def alpha_letter_to_uni_index(letter):
    letter = ord(letter.upper())
    alpha_index = letter - 64
    return alpha_index

def uni_index_to_alpha_letter(index):
    letter = chr(index)
    return letter

def alpha_to_unic_v0(alpha_letter):
    alpha_letter = str(alpha_letter).upper()
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha_index = alphabet.find(alpha_letter)
    uni_index = int(alpha_index + 65)
    #uni_letter = str(chr(uni_index))
    return uni_index #

def unic_to_alpha_v0(uni_letter):
    uni_letter = int(uni_letter)
    alpha_index = int(uni_letter - 65)
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha_letter = str(alphabet[alpha_index]).upper()
    return alpha_letter

def letter_conversion_v0(letter):
    if isinstance(letter, str):
        if len(letter) != 1 or not letter.isalpha:
            raise ValueError("Input must be a single alphabet letter.")
        else:
            return alpha_to_unic_v0(letter)
    elif isinstance(letter, int):
        if 65 <= letter <= 90:
            return unic_to_alpha_v0(letter)
        else:
            raise ValueError("Integer must between 65 and 90.")
    else:
        raise ValueError("Input must be a string (letter) or an integer (Unicode code).")

def letter_conversion(letter):
    if isinstance(letter, str):
        if len(letter) != 1 or not letter.isalpha:
            raise ValueError("Input must be a single alphabet letter.")
        else:
            return alpha_letter_to_uni_index(letter)
    elif isinstance(letter, int):
        if 65 <= letter <= 90:
            return uni_index_to_alpha_letter(letter)
        else:
            raise ValueError("Integer must between 65 and 90.")
    else:
        raise ValueError("Input must be a string (letter) or an integer (Unicode code).")

def alpha_letter_to_alpha_index(letter):
    alpha_letter = str(letter).upper()
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha_index = alphabet.find(alpha_letter)
    return alpha_index

def vigenere_index(key, ptext):
    k_index = alpha_letter_to_alpha_index(key)
    p_index = alpha_letter_to_alpha_index(ptext)
    c_index = (k_index + p_index) % 26 + 65 # needs minus 2 but that breaks things
    c_text = letter_conversion(c_index)
    return c_text

def vigenere_encrypt(key, plaintext):
    ciphertext = ''
    key_length = len(key)
    for i, char in enumerate(plaintext):
        ciphertext += vigenere_index(key[i%key_length], char)
        #print(f"{i}: {key[i%key_length]}")
    print(ciphertext)
    return ciphertext

def plaintext_index(key, ctext):
    k_index = letter_conversion(key)
    c_index = letter_conversion(ctext)
    p_index = (c_index - k_index) % 26 + 65
    p_text = letter_conversion(p_index)
    return p_text

def vigenere_decrypt(key, ciphertext):
    plaintext = ''
    key_length = len(key)
    for i, char, in enumerate(ciphertext):
        plaintext += plaintext_index(key[i%key_length], char)
    print(plaintext)
    return plaintext

#plaintext = 'SEEYOUNEXTMISSION'; keyword = 'METROID'; ciphertext = 'EIXPCCQQBMDWAVUSG'

#print(vigenere_index('M', 'S'))
vigenere_encrypt('METROID', 'SEEYOUNEXTMISSION')