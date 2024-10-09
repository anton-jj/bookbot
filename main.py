def main():
    path_to_file = "books/frankenstein.txt"
    text = get_book_text(path_to_file)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    report(char_count, word_count)

def report(char_count, word_count):
    print("Report of text starts now...")
    print(f"there is {word_count} word found in the text")
    char_list = [{"char": char, "count": count} for char, count in char_count.items()]

    char_list.sort(reverse=True, key=sort_on)    

    for item in char_list:
        if item["char"].isalpha():
            print(f"The letter '{item['char']}' is found {item['count']} times in the text.")

def sort_on(char_count):
    return char_count["count"]

def get_char_count(text): 
    lowered_text = text.lower()
    chars_count = {}
    for c in lowered_text:
        if c not in chars_count: 
            chars_count[c] = 1
        else: 
            chars_count[c] += 1
    return chars_count

def get_word_count(text): 
    words = text.split()
    return len(words)

def get_book_text(path_to_file): 
    with open(path_to_file) as f: 
        return  f.read()

main()
