def is_valid(isbn):

    cleaned = isbn.replace("-", "")

    if len(cleaned) != 10:
        return False
    total =0
    multipler = 10
    
    for index, char in enumerate(cleaned):

        if char == "X" and index == 9:
            total += 10 *multipler
        
        elif char.isdigit():
            total += int(char) * multipler

        else:
            return False

        multipler -= 1

    return total % 11  ==0
