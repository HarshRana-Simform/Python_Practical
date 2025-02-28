# 1. Write a program for computing GCD of 2 numbers with optimal data structures and less time-consuming.
#     The program should take input from console or args and should handle unexpected inputs

#     Constraints:
#         - For loop is not allowed
#         - input should be in words:
#             - e.g.: onetwo = 12, sixone = 61

#         - words will be within zero to nine
#         - Cannot use inbuilt methods like max, min, or any math function

#     Example 1:

#         - Input 1: onezero
#         - Input 2: twozero
#         - Output: onezero

#     Example 2:

#         - Input 1: twosix
#         - Input 2: twofour
#         - Output: two


import re

def words_to_number(word_str :str) -> int:
    """
    Converts a string of number words into its corresponding integer.

    Parameters:
    word_str (str): A string containing words representing a number (e.g., "onetwothree").

    Returns:
    int: The integer representation of the input number string.
    """

    # Mapping from words to numbers
    word_to_digit = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
        }

    # Defining a regular expression pattern to match any of the number words
    pattern = r"(zero|one|two|three|four|five|six|seven|eight|nine)"

    # Replace all occurrences of the words with their corresponding digits
    return int(re.sub(pattern, lambda match: word_to_digit[match.group(0)], word_str))


def gcd(a :int, b :int) -> int:
    """
    Recursively computes the Greatest Common Divisor (GCD) of two numbers using the Euclidean algorithm.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The greatest common divisor of `a` and `b`.
    """

    # Termination condition based on euclidean algorithm
    if b == 0:
        return a

    # Recursive call to set a = b and b = a%b
    return gcd(b,a%b)


def number_to_word(ans :int) -> str:
    """
    Converts a number into its corresponding word string (e.g., 12 = "onetwo").

    Parameters:
    ans (int): A number.

    Returns:
    str: The word representation of the input number.
    """

    # Mapping from numbers to words
    digit_to_word = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
        }

    result = str(ans)

    # Defining a regular expression pattern to match any of the digits
    pattern = r"(0|1|2|3|4|5|6|7|8|9)"

    # Replace all occurrences of the digits with their corresponding words
    return re.sub(pattern, lambda match: digit_to_word[match.group(0)], result)

def main():

    try:

        input1 = input("Enter input 1: ")
        if not input1.isalpha():
            raise Exception

        input2 = input("Enter input 2: ")
        if not input2.isalpha():
            raise Exception

        num1 = words_to_number(input1.lower())
        num2 = words_to_number(input2.lower())
    except:
        print('''Invalid input! Make sure your input follows the constraints:
              1. Numbers in words only in between 'zero' to 'nine'
              2. No spaces between words''')
        return


    print(number_to_word(gcd(num1,num2)))

if __name__ == '__main__':
    main()

