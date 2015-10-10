FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    'string representation of n for 0 < number < 1000'

    s = []

    while number:
        if number and number >= 100:
            # how many hunderd?
            first_ten_idx = int(str(number)[0]) - 1
            s.append(FIRST_TEN[first_ten_idx])
            s.append(HUNDRED)
            number = int(str(number)[1:])
        if number and number >= 20:
            # how many deci?
            other_tens_idx = int(str(number)[0]) - 2
            s.append(OTHER_TENS[other_tens_idx])
            number = int(str(number)[1:])
        if number and number >= 10:
            # what of second ten?
            s.append(SECOND_TEN[number-10])
            number = None
        if number and number < 10:
            s.append(FIRST_TEN[number-1])
            number = None

    return " ".join(s)


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(40) == 'forty', "6th example"
    assert checkio(40) == 'forty', "6th example"
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
