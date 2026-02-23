def is_pangram(sentence):
    cleaned = sentence.lower()
    alphabets ="abcdefghijklmnopqrstuvwxyz"

    return all(letter in cleaned for letter in alphabets)
