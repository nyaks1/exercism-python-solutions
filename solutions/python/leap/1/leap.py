def leap_year(year):

    divisible_4 = year % 4 == 0
    divisible_100 = year % 100 == 0
    divisible_400 = year % 400 == 0

    return divisible_4 and (not divisible_100 or divisible_400)