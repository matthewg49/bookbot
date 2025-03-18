def get_num_words(book_text):
    return len(book_text.split())

def get_num_characters(book_text):
    lowered = book_text.lower()
    all_chars = {}
    for c in lowered:
        if c in all_chars:
            all_chars[c] += 1
        else:
            all_chars[c] = 1
    return all_chars

def sort_on(dict):
    return dict["number"]

def sorted_characters(dictionary_of_chars):
    list_of_dicts = []
    for k in dictionary_of_chars:
        if k.isalpha():
            list_of_dicts.append({"character": k, "number": dictionary_of_chars[k]})
    
    list_of_dicts.sort(reverse=True, key=sort_on)

    for i in list_of_dicts:
        print(f"{i['character']}: {i['number']}")