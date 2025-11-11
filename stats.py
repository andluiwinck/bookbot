def count_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    char_counts = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char in char_counts:
            char_counts[lowered_char] += 1
        else:
            char_counts[lowered_char] = 1
    return char_counts

def sort_char_counts(char_counts_dict):
    def sort_on(d):
        return d["num"]

    char_list = []
    for char, count in char_counts_dict.items():
        char_list.append({"char": char, "num": count})
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list