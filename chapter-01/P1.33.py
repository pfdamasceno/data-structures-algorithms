'''
P-1.34 A common punishment for school children is to write out a sentence multiple
times. Write a Python stand-alone program that will write out the
following sentence one hundred times: “I will never spam my friends
again.” Your program should number each of the sentences and it should
make eight different random-looking typos.
'''
import random
def bart_simpson():
    sentence = "I will never spam my friends again."
    typo_index = random.sample(range(0, 99), 8) #generate 8 distinct integers in desired range

    def make_mistake(my_sentence):
        #replace 2 characters near each other
        index_1 = random.randint(0,len(my_sentence)-2)
        index_2 = index_1 + 1
        while my_sentence[index_2] == my_sentence[index_1]:
            index_1 = random.randint(0,len(my_sentence)-1)
            index_2 = index_1 + 1
        new_sentence = my_sentence[:index_1] + my_sentence[index_2] + my_sentence[index_1] + my_sentence[index_2 + 1:]
        return(new_sentence)

    for i in range(100):
        if i in typo_index:
            print(str(i) + " " + make_mistake(sentence) + "*")
        print(str(i) + " " + sentence)
