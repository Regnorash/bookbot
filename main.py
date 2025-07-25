#count the amount of words in the provided text
def count_words(text):
    return len(text.split())

#open and read the file in the provided path
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    #count and print the amount of words in Frankenstein
    num_words = count_words(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")

main()