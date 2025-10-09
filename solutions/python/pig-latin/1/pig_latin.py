def translate(text):
    vowels = ["a","e","i","o","u"]
    words = text.split()
    translated_words = []

    for word in words:
        if word[0] in vowels or word[0:2] == "xr" or word[0:2] == "yt": 
            new_text = word + "ay"
        else:
            first_vowel_index = -1
            for i, char in enumerate(word):
                if char in vowels:
                    first_vowel_index = i
                    break
                elif char == "y" and i != 0:
                    first_vowel_index = i
                    break
            if first_vowel_index == -1:
                new_text  = word + "ay"
            else:
                if word[first_vowel_index-1:first_vowel_index+1] == "qu":
                    first_vowel_index += 1
                rest_of_word = word[first_vowel_index:]
                consonant_cluster = word[:first_vowel_index]
                new_text = rest_of_word + consonant_cluster + "ay"
        translated_words.append(new_text)
        
    return " ".join(translated_words)
        
