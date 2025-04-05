def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def total_words():
    text = get_book_text("books/frankenstein.txt")
    words = text.split()
    word_count = len(words)
    return word_count

def letter_count(text):
    total_letters = {}

    for l in text.lower():
        if l not in total_letters:
            total_letters[l] = 1
        elif l in total_letters:
            total_letters[l] += 1
    return total_letters

def sort_count(letter_count):
    count_list = [{"char": char, "count": count} for (char, count) in letter_count.items()]
    count_list.sort(reverse=True, key=lambda item: item["count"])
    return count_list


