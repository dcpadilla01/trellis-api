import re

ONES = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

ONES_DICT = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six","7": "seven", "8": "eight", "9": "nine"}

TEENS = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

TENS = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

DIMENSIONS = ["", " hundred ", " thousand ", " million "]


def one_to_hundred(num):

    if num < 10:
        return ONES[num]
    elif 10 < num < 20:
        return TEENS[num-10]
    else:
        return TENS[num//10] + (" " + ONES[num % 10] if num % 10 != 0 else "")


def dimension_exists(num, num_in_amount):

    return num if num_in_amount > 0 else 0


def is_valid_number(input_string):
    pattern = r'^-?\d+(\.\d+)?$'

    if re.match(pattern, input_string):
        return True
    else:
        return False


def first_part_to_english(number_string):

    number_strings = number_string.zfill(9)

    if int(number_string) == 0:
        text = "zero"
        return text

    text = ONES[int(number_strings[0])] + \
        DIMENSIONS[dimension_exists(1, int(number_strings[0]))] + \
        one_to_hundred(int(number_strings[1:3])) + \
        DIMENSIONS[dimension_exists(3, int(number_strings[0:3]))] + \
        ONES[int(number_strings[3])] + \
        DIMENSIONS[dimension_exists(1, int(number_strings[3]))] + \
        one_to_hundred(int(number_strings[4:6])) + \
        DIMENSIONS[dimension_exists(2, int(number_strings[3:6]))] + \
        ONES[int(number_strings[6])] + \
        DIMENSIONS[dimension_exists(1, int(number_strings[6]))] + \
        one_to_hundred(int(number_strings[7:9]))

    return text


def separate_decimal_part(number_string):
    integer_part = ""
    decimal_part = ""

    separate_number = number_string.split('.') 

    integer_part = separate_number[0]

    if "." in number_string:

        decimal_part = separate_number[1]

    return integer_part, decimal_part


def has_decimal_part(decimal_part):

    return len(decimal_part) > 0


def values_if_negative_number(integer_part):
    max_string_length = 9
    start_slice = 0
    text_for_sign = ""

    if integer_part[0] == "-":
        text_for_sign = "negative "
        return max_string_length + 1, start_slice + 1, text_for_sign

    return max_string_length, start_slice, text_for_sign


def number_to_english(number):
    """Returns a string which will be 'number' converted to english.
    Only allows for numbers up to 9 characters long before the decimal point,
    not counting the negative sign, if there is one.

    Arguments:
    number - number string from the endpoint.
    """

    integer_string = ""
    decimal_string = ""

    number_string = str(number)

    if not is_valid_number(number_string):

        return "Please input a valid number with the format: '-####.####'"

    integer_part, decimal_part = separate_decimal_part(number_string)

    max_string_length, start_slice, text_for_sign = values_if_negative_number(integer_part)

    if len(integer_part) > max_string_length:

        return "Please input a smaller value."

    integer_string = first_part_to_english(integer_part[start_slice:])

    if has_decimal_part(decimal_part):
        decimal_string = " point "

        for int in decimal_part:
            decimal_string += ONES_DICT[int] + " "

    return (text_for_sign + integer_string + decimal_string).strip()
