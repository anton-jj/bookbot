def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    num_words = get_word_count(text)
    print(f"{num_words} found in document")

def get_word_count(text): 
    words = text.split()
    return len(words)
def get_book_text(path_to_file): 
    with open(path_to_file) as f: 
        return  f.read()
main()
