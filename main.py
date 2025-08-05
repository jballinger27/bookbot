
from stats import number_of_words

def get_book_text(rel_path):
    with open(rel_path) as f:
        return f.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    #print(book_text)
    print(f"{number_of_words(book_text)} words found in the document")

main()