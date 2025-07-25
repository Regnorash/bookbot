#count the amount of words in the input text
def count_words(text):
    return len(text.split())

#count the amount of times each character appears in the input text
def count_characters(text):
    characters_count = {}
    lowercase = text.lower()

    for c in lowercase:
        if not c in characters_count:
            characters_count[c] = 0
        characters_count[c] += 1
    
    return characters_count