"""Generate Markov text from text files."""

from random import choice
import sys

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as f: file_string = f.read()

    return file_string


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    # dictionary also only contains unique keys
    # chains = {}
    
    text_string = text_string.split()
    # print(text_string)

    # further study: alter the size of n-gram used
    ngram_size = 3 #for a bigram, want text_string[0:n-1]
    chain_dict = {}

    # loop through each word in text string array, and add tuple of current word + next word into chains set
    for i in range(len(text_string)-ngram_size+1):
        # chains.add((text_string[i], text_string[i+1]))
        # chains.add((text_string[i], text_string[i+ngram_size-1]))
        try:
            words_following = text_string[i+ngram_size]
        except IndexError: words_following = None
        # print(words_following)
        ngram = tuple(text_string[i:i+ngram_size])
        # print(ngram)
        ## why doesn't append.words_following work?
        chain_dict[ngram] = chain_dict.get(ngram, []) + [words_following]
        # print(chain_dict)
        

    # # loop through every ngram in our set of ngrams/key
    # for ngram in chains:
    #     # print('ngram:', ngram)
    #     words_following = []
    #     # loop through every string in the split original text string (['Would'], ['you'],...)
    #     ## stop at len - 1 so we don't get an error once we hit the last word
    #     for i in range(len(text_string)-1):
    #         try:
    #             if " ".join(text_string[i:i+ngram_size]) == " ".join(ngram[:ngram_size]):
    #                 # print(text_string[i+2])
    #                 words_following.append(text_string[i+ngram_size])
    #                 # print('words following:', words_following)
    #         except IndexError: pass
        # chain_dict[ngram] = words_following

    for mkv in chain_dict: print(mkv, ":", chain_dict[mkv])

    return chain_dict

def make_text(chains):
    """Return text from chains."""

    our_string = []
    ## current_tuple = ('could', 'in') ## use choice on list of keys to avoid hardcoding
    # print(list(chains.keys()))
    current_tuple = choice(list(chains.keys()))
    # print(f"\ncurrent tuple = {current_tuple}")
    # print(f"dictionary entry = {chains[current_tuple]}")
    nextword = "llama"

    our_string = " ".join(current_tuple)


    while nextword != None:
    # while current_tuple != ("I", "am"):
        try:
            nextword = choice(chains[current_tuple])

            # print("----------------------------------------\n",
            #     f"current tuple = {current_tuple}\n",
            #      f"dictionary entry = {chains[current_tuple]}\n",
            #      f"next word = {nextword}\n")

            next_tuple = (*current_tuple[1:], nextword)
            # next_tuple = current_tuple[1:] + (nextword,)

            our_string += f" {nextword}"
            current_tuple = next_tuple
        except IndexError: break
        # except KeyError: break
    # print(our_string)
    return our_string


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
