def response(hey_bob):
    cleaned = hey_bob.strip()

    if cleaned == "":
        return "Fine. Be that way!"

    if cleaned.isupper() and cleaned.endswith("?"):
        return "Calm down, I know what I'm doing!"

    if cleaned.isupper():
        return "Whoa, chill out!"

    if cleaned.endswith("?"):
        return "Sure."

    return "Whatever." 
    
            
    
