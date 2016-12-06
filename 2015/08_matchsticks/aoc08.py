"""Matchsticks

Advent of Code 2015, day 8
Solution by Geir Arne Hjelle, 2016-12-06
"""
import sys

def memory(words):
    modified_words = list()
    for word in words:
        word = word[1:] if word.startswith('"') else word
        word = word[:-1] if word.endswith('"') else word
        word = word.replace('\\\\', '_')
        word = word.replace('\\"', '"')
        while '\\x' in word:
            idx = word.index('\\x')
            word = word[:idx] + chr(int(word[idx+2:idx+4], 16)) + word[idx+4:]

        modified_words.append(word)

#    for word, mword in zip(words, modified_words):
#        print('{:44s} {:2d}  {:33s} {:2d}'.format(word, len(word), mword, len(mword)))

    return modified_words


def encoded(words):
    encoded_words = list()
    for word in words:
        word = word.replace('\\', '\\\\')
        word = word.replace('"', '\\"')
        encoded_words.append('"' + word + '"')

#    for word, eword in zip(words, encoded_words):
#        print('- {:74s} {:2d}\n  {:74s}    {:2d}'.format(word, len(word), eword, len(eword)))

    return encoded_words



def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            words = [l.strip() for l in fid]

        len_string_literal = sum(len(w) for w in words)
        len_in_memory = sum(len(w) for w in memory(words))
        print('Literal vs memory length:  {} - {} = {}'.format(len_string_literal, len_in_memory,
                                                               len_string_literal - len_in_memory))
        len_encoded = sum(len(w) for w in encoded(words))
        print('Encoded vs literal length: {} - {} = {}'.format(len_encoded, len_string_literal,
                                                               len_encoded - len_string_literal))

if __name__ == '__main__':
    main()
