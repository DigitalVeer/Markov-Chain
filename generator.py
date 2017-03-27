import prefix
import suffix



def get_word_list(chain, pref, f_random, num_words, nonword):
    curr_vals = []
    return get_word_list_helper(chain, pref, f_random, num_words, nonword, 0, curr_vals)

def get_word_list_helper(chain, pref, f_random, num_words, nonword, count, list):
    if count == num_words:
        return tuple(list)
    rand_word = suffix.choose_word(chain, pref, f_random)
    list.append(rand_word)
    new_pref = prefix.shift_in(pref, rand_word)
    return get_word_list_helper(chain, new_pref, f_random, num_words, nonword, count + 1, list)


def generate(chain, f_random, num_words, nonword):
    starting_pref = ("\n", "\n")
    words = get_word_list(chain, starting_pref, f_random, num_words, nonword)
    return ' '.join(words)
