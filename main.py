from stats import count_words, get_char_counts

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_text = f.read()
    return book_text

def main():
    
    book_path = "books/frankenstein.txt"
    
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_counts = get_char_counts(text)
    
    print(f"Found {num_words} total words")
    print(char_counts)

main()