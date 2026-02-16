def translate(text):
    translated_words = []
    
    for word in text.split():

        cleaned_word = word.lower() 

        if cleaned_word.startswith(('a', 'e', 'i', 'o', 'u', 'xr', 'yt')):
            translated_words.append(cleaned_word + "ay")
            continue 
            
        
        for i, char in enumerate(cleaned_word):
         
            if char == 'u' and cleaned_word[i-1] == 'q':
                continue 

            if char in "aeiou":
                split_index = i
                break 
                
            if char == 'y' and i > 0:
                split_index = i
                break 
        
        new_word = cleaned_word[split_index:] + cleaned_word[:split_index] + "ay"
        translated_words.append(new_word)

    return " ".join(translated_words)