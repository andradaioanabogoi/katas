# How many times does this word appear in the book?
# If we have to run this method multiple times, it's worth doing some pre-processing on the book
# i.e. to create a dictionary with all the words in the book and finally to lookup (O(1) runtime) the desired word


def create_dict(book):
    output = {}
    for word in book:
        word = word.lower().strip()
        if(word != ""):
            if(word not in output):
                output[word] = 1
            else:
                output[word] = output[word] + 1
    return output


def word_frequencies(book, word):
    _dict = create_dict(book)
    return _dict[word]


print(word_frequencies(["hii", "hii", "ada"], "hii"))
