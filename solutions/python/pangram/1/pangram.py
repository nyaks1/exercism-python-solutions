def is_pangram(sentence):
    cleaned = sentence.lower()
    alphabets ="abcdefghijklmnopqrstuvwxyz"

    for letter in alphabets:
        if letter not in cleaned:
            return False
    return True
