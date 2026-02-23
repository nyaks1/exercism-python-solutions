def is_isogram(string):
    letters = string.replace("-", "").replace(" ", "").lower()
    letters_list = list(letters)
    uni = set(letters)

    if len(letters_list) == len(uni):
        return True
    return False
        
