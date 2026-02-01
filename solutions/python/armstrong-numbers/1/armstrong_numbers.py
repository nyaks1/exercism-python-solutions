def is_armstrong_number(number):
    total = 0
    for number_str in str(number):
        square = int(number_str) ** int(len(str(number)))
        total += square
    if total == number:
        return True
    else:
        return False 
        
