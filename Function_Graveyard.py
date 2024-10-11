def alpha_letter_to_uni_index(letter):
    letter = ord(letter.upper())
    alpha_index = letter - 64
    return alpha_index

def uni_index_to_alpha_letter(index):
    letter = chr(index)
    return letter

def index_conversion(letter):
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

def alphabet_to_unicode(alpha_letter):
    alpha_letter = str(alpha_letter).upper()
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha_index = alphabet.find(alpha_letter)
    uni_index = int(alpha_index + 65)
    return uni_index

def unicode_to_alphabet(uni_letter):
    uni_letter = int(uni_letter)
    alpha_index = int(uni_letter - 65)
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alpha_letter = str(alphabet[alpha_index]).upper()
    return alpha_letter

def letter_conversion(letter):
    if isinstance(letter, str):
        if len(letter) != 1 or not letter.isalpha:
            raise ValueError("Input must be a single alphabet letter.")
        else:
            return alphabet_to_unicode(letter)
    elif isinstance(letter, int):
        if 65 <= letter <= 90:
            return unicode_to_alphabet(letter)
        else:
            raise ValueError("Integer must between 65 and 90.")
    else:
        raise ValueError("Input must be a string (letter) or an integer (Unicode code).")
