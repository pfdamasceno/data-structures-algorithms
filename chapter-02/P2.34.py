import string
from collections import Counter #for counting the occurence of a character
import matplotlib.pyplot as plt

text_doc = open('./random_wiki.txt')

class Text():
    def __init__(self, new_document):
        self.ASCII_CHARS = list(string.ascii_letters+string.digits)
        self.ascii_dict  = dict((k, 0) for k in self.ASCII_CHARS)
        self.document = new_document

    def calculate_histogram(self):
        for line in self.document:
            char_list = list(line)
            for c in char_list:
                try:
                    self.ascii_dict[c] += 1
                except:
                    print('character not a number or letter')

    def plot_barchart(self):
        characters = list(self.ascii_dict.keys())
        frequency  = list(self.ascii_dict.values())

        plt.bar(characters, frequency, align='center', alpha=0.7)
        plt.xticks(characters, fontsize=8)
        plt.ylabel('Character Frequency')
        plt.xlabel('Character')
        plt.title('Character frequency in random wiki article')

        plt.show()


if __name__ == "__main__":
    #testing
    random_wiki = Text(text_doc)
    random_wiki.calculate_histogram()
    random_wiki.plot_barchart()
