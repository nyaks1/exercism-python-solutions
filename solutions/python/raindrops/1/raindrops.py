def convert(number):

    results = ""

    if number % 3 == 0:
        results += "Pling"

    if number % 5 == 0:
        results += "Plang"

    if number % 7 == 0:
        results += "Plong"

    return results or str(number)