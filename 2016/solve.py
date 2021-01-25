def solve_1(num):
    """
    4進数の数を読み取り10進数で表示する
    """
    ans = 0
    for i,n in enumerate(list(str(num))):
        ans += int(n) * 4**(len(str(num))-i-1)
    print(ans)


def solve_2(s):
    str_to_num = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4,
        "f": 5,
        "g": 6,
        "h": 7
    }
    ans = 0
    for i,n in enumerate(list(s)):
        ans += str_to_num[n] * 8**(len(s)-i-1)
    print(ans)

special = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900,
}
normal = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def parse_roman_numerals(roman_numeral):
    """
    >>> parse_roman_numerals("II")
    2
    >>> parse_roman_numerals("CCVII")
    207
    >>> parse_roman_numerals("MLXVI")
    1066
    >>> parse_roman_numerals("MCMIV")
    1904
    """
    ans = 0
    used = []
    for i in range(len(roman_numeral)-1):
        tmp = roman_numeral[i:i+2]
        if tmp in special.keys():
            ans += special[tmp]
            used.extend([i,i+1])
    for j in range(len(roman_numeral)):
        if j not in used:
            ans += normal[roman_numeral[j]]

    return ans


def convert_to_roman_numerals(num):
    """
    >>> convert_to_roman_numerals(2)
    'II'
    >>> convert_to_roman_numerals(207)
    'CCVII'
    >>> convert_to_roman_numerals(1066)
    'MLXVI'
    >>> convert_to_roman_numerals(1904)
    'MCMIV'
    """
    special_reverse = {} 
    for k, v in special.items():
        special_reverse[v] = k
    normal_reverse = {} 
    for k, v in normal.items():
        normal_reverse[v] = k
    ans = ""
    for i, n in enumerate(list(str(num))):
        tmp = int(n) * 10**(len(str(num))-i-1)
        if tmp in special_reverse.keys():
            ans += special_reverse[tmp]
        elif int(n) != 0:
            if int(n) < 5:
                ans += normal_reverse[tmp/int(n)] * int(n)
            elif int(n) == 5:
                ans += normal_reverse[tmp]
            else:
                ans += normal_reverse[5*(10**(len(str(num))-i-1))] \
                    + normal_reverse[10**(len(str(num))-i-1)] * (int(n)-5)
    return ans


# def ex_roman_numerals(num):
#     """
#     >>> ex_roman_numerals(149)
#     'CIL'
#     """

english_nums = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, 
    "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
    "eleven": 11, "twelve": 12, "thirteen": 13, "forteen": 14, "fifteen": 15,
    "sixteen": 16, "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
    "thirty": 30, "fourty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
    "eighty": 80, "ninty": 90, "hundred": 100, "thousand": 1000
}


def parse_english_num(s):
    """
    >>> parse_english_num("fifty four thousand three hundred twelve")
    54312
    >>> parse_english_num("one thousand two hundred")
    1200
    >>> parse_english_num("one")
    1
    >>> parse_english_num("eleven")
    11
    >>> parse_english_num("two thousand")
    2000
    >>> parse_english_num("three thousand two")
    3002
    >>> parse_english_num("one hundred ninty")
    190
    >>> parse_english_num("eleven thousand twenty two")
    11022
    >>> parse_english_num("one thousand one hundred twenty two")
    1122
    """
    words = s.split(" ")
    ans = 0
    tidx = 0
    hidx = 0
    if "thousand" in words and "hundred" in words:
        tidx = words.index("thousand")
        hidx = words.index("hundred")
        tmp = 0
        for w in words[:tidx]:
            tmp += english_nums[w]
        ans += tmp*1000
        for w in words[tidx+1:hidx]:
            tmp = 0
            tmp += english_nums[w]
        ans += tmp*100
        for w in words[hidx+1:]:
            ans += english_nums[w]
    elif "thousand" in words:
        tidx = words.index("thousand")
        tmp = 0
        for w in words[:tidx]:
            tmp += english_nums[w]
        ans += tmp*1000
        for w in words[tidx+1:]:
            ans += english_nums[w]
    elif "hundred" in words:
        hidx = words.index("hundred")
        tmp = 0
        for w in words[:hidx]:
            tmp += english_nums[w]
        ans += tmp*100        
        for w in words[hidx+1:]:
            ans += english_nums[w]   
    else:
        for w in words:
            ans += english_nums[w]
    return ans


if __name__ == "__main__":
    solve_1(123)
    solve_2("bcd")
    parse_roman_numerals("MCMIV")
    import doctest
    doctest.testmod()
    convert_to_roman_numerals(207)
    parse_english_num("fifty four thousand three hundred twelve")