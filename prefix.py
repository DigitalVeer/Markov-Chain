
def new_prefix(word_one, word_two):
    return (word_one, word_two)


def shift_in(word_tup, word_pivot):
    shifted_word = word_tup[1]
    new_tup = new_prefix(shifted_word, word_pivot)
    return new_tup
