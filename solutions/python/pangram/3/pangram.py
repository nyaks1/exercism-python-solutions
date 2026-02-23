def is_pangram(sentence):
    """Checks if a sentence is a pangram """
    cleaned = sentence.lower()
    alphabets ="abcdefghijklmnopqrstuvwxyz"

    return all(letter in cleaned for letter in alphabets)
