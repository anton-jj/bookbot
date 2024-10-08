def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_words = get_word_count(text)
    number_chars = get_char_count(text)
    print(number_chars)
    print(f"{num_words} found in document")

def get_char_count(text): 
    lowered_text = text.lower()
    chars_count = {}
    for c in lowered_text:
        if c not in chars_count: 
            chars_count[c] = 1
        else: 
            chars_count[c] += +1
    return chars_count

def get_word_count(text): 
    words = text.split()
    return len(words)

def get_book_text(path_to_file): 
    with open(path_to_file) as f: 
        return  f.read()

main()
