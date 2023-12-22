import re

ONES = ["","one","two","three","four","five","six","seven","eight","nine"]

TEENS = ["","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

TENS = ["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]


def is_only_numbers(input_string):
    pattern = r'^\d+$'
    
    if re.match(pattern, input_string):
        return True
    else:
        return False


def number_to_english(number_str):

    if not is_only_numbers(number_str):
        return "Please input only digits"
    
    number = int(number_str)

    number_length = len(number)

    pattern_called = pattern[number_length](place=2)

    return pattern_called


