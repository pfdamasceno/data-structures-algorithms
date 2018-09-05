'''
P-1.36 Write a Python program that inputs a list of words, separated by whitespace,
and outputs how many times each word appears in the list. You
need not worry about efficiency at this point, however, as this topic is
something that will be addressed later in this book.
'''
def count_words(text):
    '''
    input: str(text) = text in the form of a string
    output: dict(word_count) = dictionary of words as well as the number of occurences in the text
    '''
    words = [i.lower() for i in text.split()]
    word_set = set(words)
    count_dic = {}
    for w in word_set:
        count_dic[w] = 0

    for w in words:
        count_dic[w] += 1

    return(count_dic)

if __name__ == "__main__":
    print(count_words("Write a Python program that inputs a list of words, separated by whitespace, and outputs how many times each word appears in the list. You need not worry about efficiency at this point, however, as this topic is something that will be addressed later in this book."))








#
