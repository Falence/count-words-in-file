# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    with open(filename, encoding='utf-8') as f:
        contents = f.read()   
        return contents


def count_words():
    text = read_file_content("./story.txt").lower()
    word_dictionary = {}

    words = text.split()
    for word in words:
        word_count = words.count(word)
        word_dictionary[word] = word_count

    return word_dictionary

print(count_words())