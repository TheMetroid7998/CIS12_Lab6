import sys

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

def alpha_letter_to_alpha_index(letter):
    """Converts an alphabetic letter to an index in range 0 - 25."""
    alpha_letter = str(letter).upper()
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha_index = alphabet.find(alpha_letter)
    return alpha_index

def alpha_index_to_alpha_letter(number):
    """Converts an index value in range 0 - 25 to an alphabetic letter."""
    alpha_index = int(number)
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha_letter = alphabet[alpha_index]
    return alpha_letter

def letter_conversion(letter):
    """Determines the type of input, validates it, and passes to the appropriate conversion function."""
    if isinstance(letter, str):
        if len(letter) != 1 or not letter.isalpha:
            raise ValueError("Input must be a single alphabet letter.")
        else:
            return alpha_letter_to_alpha_index(letter)
    elif isinstance(letter, int):
        if 0 <= letter <= 25:
            return alpha_index_to_alpha_letter(letter)
        else:
            raise Exception("Integer must between 0 and 25.")
    else:
        raise Exception("Input must be a string or an integer.")

def vigenere_index(key, ptext):
    """Converts a single letter from the key and the plaintext and returns a matching ciphertext letter."""
    k_index = letter_conversion(key)
    p_index = letter_conversion(ptext)
    c_index = (k_index + p_index) % 26
    c_text = letter_conversion(c_index)
    return c_text

def vigenere_encrypt(key, plaintext):
    """Encrypts plaintext with a key.
    |>>> vigenere_encrypt('KEYWORD', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    KFAWICZRMHDPJGYTOKWQNFAVRD
    """
    ciphertext = ''
    key_length = len(key)
    for i, char in enumerate(plaintext):
        ciphertext += vigenere_index(key[i%key_length], char)
    return ciphertext, print(f"Your encrypted text is {ciphertext}.")

def plaintext_index(key, ctext):
    """Converts a single letter from the key and the ciphertext and returns a matching plaintext letter."""
    k_index = letter_conversion(key)
    c_index = letter_conversion(ctext)
    p_index = (c_index - k_index) % 26
    p_text = letter_conversion(p_index)
    return p_text

def vigenere_decrypt(key, ciphertext):
    """Decrypts ciphertext with a key.
    |>>> vigenere_decrypt('KEYWORD', 'KFAWICZRMHDPJGYTOKWQNFAVRD')
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    """
    plaintext = ''
    key_length = len(key)
    for i, char, in enumerate(ciphertext):
        plaintext += plaintext_index(key[i%key_length], char)
    return plaintext, print(f"Your decrypted text is {plaintext}.")

def manual_end():
    """Collects input to determine whether to convert another text string."""
    desire = input("Encrypt or Decrypt again?\n").upper().strip()
    if desire == 'Y':
        vigenere_conversion()
    elif desire == 'N':
        sys.exit()
    else: # desire != 'N' or desire != 'Y':
        print("Enter only 'Y' or 'N' to indicate your preference.")
        manual_end()

def vigenere_conversion():
    """Collects the plain/ciphertext, the key, and input to encrypt or decrypt the text with the appropriate function."""
    try:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        print(f"MAIN MENU\nPlease select Play to start the movie- no wait that's not right...")
        text = input("Please enter the text you wish to encrypy or decrypt:\n").upper().strip()
        if not all(char in alphabet for char in text):
            raise Exception("Spaces, numbers, and other ASCII symbols are not valid for this operation.")

        key = input("Please enter the key to encrypt or decrypt this text with:\n").upper().strip()
        if not all(char in alphabet for char in text):
            raise Exception("Spaces, numbers, and other ASCII symbols are not valid for this operation.")

        mode = input(f"""Do you want to encrypt or decrypt this text?\n'E' to encrypt, 'D' to decrypt.\n""").upper().strip()
        if mode == 'E':
            vigenere_encrypt(key, text)
        if mode == 'D':
            vigenere_decrypt(key, text)
        if mode != 'E' and mode != 'D':
            raise Exception("Invalid input. Please select a valid option.")
    except Exception as error:
        print(f"An error occurred.\n{error}\nLet's try again.")
        vigenere_conversion()
    finally:
        manual_end()

vigenere_conversion()