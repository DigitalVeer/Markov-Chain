from immdict import ImmDict
from functools import reduce


def empty_suffix():
    return ImmDict()

def add_word(suffix, word):

    if  (word in suffix.keys()):
        word_freq = suffix.get(word)
        return suffix.put(word, word_freq + 1)
    else:
       return suffix.put(word, 1)


def choose_word(chain, prefix, randomizer):
    suffix = chain.get(prefix)
    if not suffix:
        return "\n"
    all_words = list(reduce(lambda x, y: x + y, map(lambda x: [x] * suffix.get(x), suffix.keys())))
    rand_val = randomizer(len(all_words))
    rand_word = all_words[rand_val - 1]
    return rand_word
