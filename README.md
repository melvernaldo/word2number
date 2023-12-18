# word2number

This is a python module to convert worded numbers ("Three hundred and eleven") to an integer (12). This works for positive and negative integers up to 999,999,999,999,999 (10^12 - 1) and down to its negative.

The module contains the `word2number` function that is intended for use. Other functions in the module are for the `word2number` function to access.

The main function `word2number` of this module can receive an iterable object of strings, e.g. list of strings or Numpy's array of strings which it then returns a list of parsed integers. It can also receive just a string, which will return the parsed integer.

The input of the function is case-insensitive.

This module might require Numpy if the input string is 'nan' which will return Numpy's NaN.

## Usage

To use this module, you first have to at least import the `word2number` function from the module.

```
from word2number import word2number
```

The following are examples of using the function.

```
print(word2number("Three thousand four hundred and eleven"))
3411
```

```
print(word2number("One million and twelve thousand"))
1012000
```

```
print(word2number(["Negative three million and twenty one", "thirteen hundred"]))
[-3000021, 1300]
```

```
print(word2number("OnE BiLLioN"))
1000000000
```

### Notes

- If the input is not a string or an iterable containing _only_ strings, the function will raise a `TypeError` and stops the program.

```
print(word2number(3))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/user/code/python/word2number/word2number.py", line 149, in word2number
    raise TypeError("This function only accepts string or list of strings!")
TypeError: This function only accepts string or list of strings!
```

```
print(word2number( ["One", "two", 3] ))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/user/code/python/word2number/word2number.py", line 147, in word2number
    raise TypeError("This function only accepts string or list of strings!")
TypeError: This function only accepts string or list of strings!
```

- The string 'nan' (case insensitive) will be parsed as Numpy's NaN.
  Examples:

  ```
  word2number('nan')
  nan
  ```

  ```
  word2number('NaN')
  nan
  ```

- An empty string will be parsed as the integer 0
  Examples:

  ```
  word2number('')
  0
  ```

  ```
  word2number(['three', ''])
  [3, 0]
  ```

- Any words that can't be individually parsed as a number will be ignored and trigger
  a runtime warning but will still returns the parsed integer/s.
  Examples:

  ```
  print(word2number('test'))
  <stdin>:1: RuntimeWarning: One or more invalid words are ignored! Check your input!
  0
  ```

  ```
  print(word2number('Three Ligmas'))
  <stdin>:1: RuntimeWarning: One or more invalid words are ignored! Check your input!
  3
  ```

- The word 'and' is an exception of the last point. It will be ignored but
  will not trigger a warning.
