import doctest

def run_doctests(func):
    doctest.run_docstring_examples(func, globals())

"""Exercise 7.9.2"""

def uses_none(word, forbidden):
    """Checks whether a word avoids forbidden letters.

    >>> uses_none('banana', 'xyz')
    True
    >>> uses_none('apple', 'efg')
    False
    >>> uses_none('steak', '1923')
    True
    >>> uses_none('Windows 11', '9 e')
    False
    """
    for letter in word.lower():
        if letter in forbidden.lower():
            return False
    return True

run_doctests(uses_none)

"""Exercise 7.9.3"""

def uses_only(word, char_str):
    """Checks whether a word uses only the available letters.

        >>> uses_only('banana', 'ban')
        True
        >>> uses_only('apple', 'apl')
        False
        >>> uses_only('racecar', 'cereal')
        True
        """
    if not all(char in char_str.lower() for char in word):
            return False
    return True

"""Exercise 7.9.4"""

def uses_all(string, char_list):
    """Checks whether a word uses all required letters.

    >>> uses_all('banana', 'ban')
    True
    >>> uses_all('apple', 'api')
    False
    >>> uses_all('racecar', 'cereal') # how to make this require the 'L' as well?
    True
    """
    if all(char in char_list.lower() for char in string):
            return True
    return False

"""Exercise 7.9.5"""

def check_word(word, available, required):
    """Check whether a word is acceptable.

    >>> check_word('color', 'ACDLORT', 'R')
    True
    >>> check_word('ratatat', 'ACDLORT', 'R')
    True
    >>> check_word('rat', 'ACDLORT', 'R')
    False
    >>> check_word('told', 'ACDLORT', 'R')
    False
    >>> check_word('bee', 'ACDLORT', 'R')
    False
    """
    if len(word) <= 3:
        #print("Words less than three characters are not valid!")
        return False
    if len(available) != 7 or len(required) != 1:
        #print("Please enter seven available characters and one required character!")
        return None
    if all(char in available.lower() for char in word.lower()):
        if any(char in required.lower() for char in word.lower()):
            return True
    return False

def word_score(word, available):
    """Compute the score for an acceptable word.

    >>> word_score('card', 'ACDLORT')
    1
    >>> word_score('color', 'ACDLORT')
    5
    >>> word_score('cartload', 'ACDLORT')
    15
    """
    score = 0

    word = word.lower()
    available = available.lower()

    if len(word) == 4:
        score = 1
    elif len(word) > 4:
        score = len(word)

    if all(char in word for char in available):
        score += 7

    return score

"""Exercise 7.9.6"""

def uses_any(word, chars):
    if any(char in chars.lower() for char in word):
            return True
    return False

def uses_not_all(word, forbidden):
    """Checks whether a word avoids forbidden letters.

        >>> uses_none('banana', 'xyz')
        True
        >>> uses_none('apple', 'efg')
        False
        >>> uses_none('', 'abc')
        True
    """
    return not uses_any(word, forbidden)

def uses_every(word, chars):
    """Checks whether a word uses all required letters.

        >>> uses_all('banana', 'ban')
        True
        >>> uses_all('apple', 'api')
        False
        >>> uses_all('racecar', 'cereal') # how to make this require the 'L' as well?
        True
        """
    return not uses_only(word, chars)

"""Exercise 7.9.8"""

def uses_any_ai(word, letters):
    return any(letter in word for letter in letters)

def uses_all_ai(word, letters):
    for letter in set(letters):
        if not uses_any_ai(word, letter * letters.count(letter)):
            return False
    return True