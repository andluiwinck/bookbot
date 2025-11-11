def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_text = f.read()
    return book_text

def count_words(text):
    words = text.split()
    return len(words)

def main():
    
    book_path = "books/frankenstein.txt"
    
    text = get_book_text(book_path)
    num_words = count_words(text)
    
    print(f"Found {num_words} total words")

main()