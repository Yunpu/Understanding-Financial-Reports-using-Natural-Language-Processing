import string
import sys
import re

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

# reading and tokenizing the file
arguments = sys.argv[1:]
filename = arguments[0]
f = open(filename).read()
f = re.sub(r'\-+', '.', f)
print(f)
sentences = sent_tokenize(f)
my_sentence = []

# defining word list

word_list = ["notional amount", "Notional Amount", "pays", "Receive"]


def sentenceFinder(sentences, word_list):
    for word in word_list:
        for sent in sentences:
            if word in sent:
                my_sentence.append(sent)
    print(my_sentence)

    return my_sentence


output = sentenceFinder(sentences, word_list)

# writing the output to the file
with open('output.txt', 'w') as f:
    for sentence in output:
        f.write("%s\n" % sentence)
