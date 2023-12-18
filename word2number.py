import numpy as np
import warnings
from collections.abc import Iterable


def parseNumberFromWord(word):
    """Parse a number from a word (SINGULAR WORD!)
    Works up to the word 'trillion'.
    Returns the parsed integer.

    Example:
    parseNumberFromWord('sixty') -> 60
    parseNumberFromWord('million') -> 1000000
    parseNumberFromWord('eighteen') -> 18

    Note: Any words not in the keywords dict, such as "and", returned as None

    """
    word = word.lower()
    keywords = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
        'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13,
        'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
        'seventeen': 17, 'eighteen': 18, 'nineteen': 19,
        'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50,
        'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90,
        'hundred': 100, 'thousand': 1000, 'million': 1000000,
        'billion': 1000000000, 'trillion': 1000000000000,
        'negative': (-1), 'and': 0
    }
    return keywords.get(word)


def _word2number(words):
    """Parse an integer from worded number. Works up to (10^12 - 1).
    Returns the parsed integer.

    Example:
    word2number('Three thousand four hundred and eleven') -> 3411

    Note: Numpy's NaN value is kept as NaN.

    """
    words = str(words)
    words = words.lower()
    if words == 'nan':
        return np.nan

    # Produce an array of numbers, each number parsed word by word.
    # 'Three thousand' -> [3, 1000]
    # 'Four hundred and twelve' -> [4, 100, 12]
    # 'Four hundred and thirty five' -> [4, 100, 30, 5]
    words_array = words.split()
    number_array = []
    for word in words_array:
        number_array.append(parseNumberFromWord(word))

    while None in number_array:
        warnings.warn("One or more invalid words are ignored! Check your input!", RuntimeWarning, stacklevel=3)
        number_array.remove(None)

    # Parse the integer from the array of numbers
    negative = False
    try:
        if number_array[0] == -1:
            negative = True
            number_array.pop(0)
    except:
        pass
        
    number_array = number_array[::-1]
    number = 0
    multiplier = 1
    for i in number_array:
        if i > 100:
            multiplier = i
        elif i == 100:
            multiplier *= i
        else:
            number += i * multiplier
    if negative:
        number = -number
    return number


def word2number(words_list):
    """Parse an integer from worded number. Works up to 10^12 - 1 (One Quadrillion - 1).
    Returns the parsed integer.

    If any iterable type is received such as a list of strings or Numpy's array
    of strings, the function returns a list of parsed integers.

    Argument:
    words_list -- a string or a list of strings to be parsed (case insensitive)

    Output:
    parsed_numbers -- an integer or a list of integers

    Examples:
    word2number('Three thousand four hundred and eleven')
    returns: 3411

    word2number(
        np.array(
            [
                'Three hundred and twelve',
                'Five hundred thirteen thousand'
            ]
        )
    )
    returns [312, 513000]

    Notes:
    - The string 'nan' (case insensitive) will be parsed as Numpy's NaN.
      Examples:
        word2number('nan') -> np.NaN
        word2number('NaN') -> np.NaN
      
    - An empty string will be parsed as the integer 0
      Examples:
        word2number('') -> 0
        word2number(['three', '']) - [3, 0]
      
    - Any words that can't be individually parsed as a number will be ignored and trigger
      a runtime warning.
      Examples:
        word2number('test')
        -> `RuntimeWarning: One or more invalid words are ignored! Check your input!`
        returns -> 0
        
        word2number('and three ligma')
        -> `RuntimeWarning: One or more invalid words are ignored! Check your input!`
        returns -> 3
        
    - The word 'and' is an exception of the last point. It will be ignored but
      will not trigger a warning.
    """
    
    # Check if the input is a string of an iterable object containing only strings
    if isinstance(words_list, str):
        return _word2number(words_list)
    
    if isinstance(words_list, Iterable):
        for word in words_list:
            if not isinstance(word, str):
                raise TypeError("This function only accepts string or list of strings!")
    else:
        raise TypeError("This function only accepts string or list of strings!")
            
        
        
    parsed_numbers = []
    for word in words_list:
        parsed_numbers.append(_word2number(word))
    return parsed_numbers
