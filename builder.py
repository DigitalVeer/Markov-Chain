import suffix
import prefix
from functools import reduce

NONWORD = "\n"

def build(file_name):
    chain_pairs = pairs_gen(file_name, line_gen)
    final_chain = build_chain(add_to_chain, chain_pairs, suffix.empty_suffix())
    return final_chain

def build_chain(f_prefix, gen_obj, imm_dict):
    fin_chain = reduce(lambda x, y: f_prefix(x, y), gen_obj, imm_dict)
    return fin_chain

def add_to_chain(chain, word_pair):
    pre = word_pair[0] #Tuple
    suff = word_pair[1] #Word

    if not (pre in chain.keys()):
        new_suf = suffix.add_word(suffix.empty_suffix(), suff)
        new_chain = chain.put(pre, new_suf)
    else:
        curr_suf = suffix.add_word(chain.get(pre), suff)
        new_chain = chain.put(pre, curr_suf)

    return new_chain


def line_gen(file_name):
    with open(file_name) as file:
        for line in file:
            yield line


def pairs_gen(file_name, f_line_gen):
    curr_prefix = prefix.new_prefix(NONWORD, NONWORD)
    line_gen = f_line_gen(file_name)

    for line in line_gen:
        words = iter(line.split())
        for word in words:
            yield (curr_prefix, word)
            curr_prefix = prefix.shift_in(curr_prefix, word)
        yield (curr_prefix, NONWORD)

