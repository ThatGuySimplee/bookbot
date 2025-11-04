def num_words(text):
    wordlist = text.split()
    return len(wordlist)

def num_char(text):
    char_count = {}
    for l in text:
        lowered = l.lower()
        if lowered in char_count:
            char_count[lowered] +=1
        else:
            char_count[lowered] = 1

    return char_count