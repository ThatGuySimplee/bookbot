def get_num_words(text):
    wordlist = text.split()
    return len(wordlist)

def get_num_char(text):
    char_count = {}
    for l in text:
        lowered = l.lower()
        if lowered in char_count:
            char_count[lowered] +=1
        else:
            char_count[lowered] = 1

    return char_count

def get_sorted(letters):
    sort_list = []
    for l in letters:
        sorting = {}
        if l.isalpha() == True:
            sorting["char"] = l
            sorting["num"] = letters[l]
            sort_list.append(sorting)
    return sort_list

def sort_on(items):
    return items["num"]