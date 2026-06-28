import re

def validate_numeric_str(string):
    post = re.sub("\d", "", string)
    return len(post) == 0


def calc_dv(numeric_id: int):
    multipliers = [2,3,4,5,6,7]
    result = 0

    digits = list(map(int, list(str(numeric_id))[::-1]))

    for index, val in enumerate(digits):
        result = result + val*multipliers[index%6]


    return (11 - result % 11) % 11