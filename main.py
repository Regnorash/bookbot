from stats import count_words
from stats import count_characters

#open and read the provided file
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    book_path = "books/frankenstein.txt"

    #get the full text of the book
    book_text = get_book_text(book_path)

    #count the amount of words in the book
    num_words = count_words(book_text)

    #count the amount of times each character appears in the book
    characters_count = count_characters(book_text)

    #print the results
    print(f"{num_words} words found in the document")
    print(characters_count)

main()