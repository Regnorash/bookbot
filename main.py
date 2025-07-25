#open and read the file in the provided path
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    #print the contents of Frankenstein
    print(get_book_text("books/frankenstein.txt"))

main()