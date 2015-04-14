import sys


def make_chains():
    """Takes input text as string; returns dictionary of markov chains."""
    # 1. open the text file, assign it to a variable
    # 2. read entire text as one string, strip of punctuation and \n
    # 3. turn entire string into list separated by " "
    # 4. Iterate through the list of words, and:
    #       - create a tuple of bigrams
    #       - add the bigram to a dictionary as a key
    #       - take the word following the bigram and make it the 
    #         value which is a list containing the word 
    #           - if there is already that bigram in the dictionary, then append
    #             the list with the word
    #       - make a conditional that has the for loop stop if there are no words 
    #         following the tuple that was just made (if index of 2nd word in 
    #         tuple == len of list, then stop)

    text_file = open("green-eggs.txt")

    text_string = text_file.read().replace("\n", " ").lower().rstrip()

    text_no_punct = ""

    for char in text_string:
        if char.isalpha() or char == " ":
            text_no_punct += char

    word_list = text_no_punct.split(" ")

    bigrams = dict() 
    # also bigrams = {} works
    for index, current_word in enumerate(word_list):
        second_word = word_list[index + 1]
        if index + 1 == len(word_list) - 1:
            break
        third_word = word_list[index + 2]



    # alist = [1, 2]
    # tups = tuple(alist)
    # prints (1, 2)
 
    return {}

make_chains()
def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    return "Here's some random text."


# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

input_text = "Some textSome textSome textSome textSome textSome textSome textSome textSome textSome textSome textSome textSome textSome text"

# Get a Markov chain
#chain_dict = make_chains(input_text)

# Produce random text
# random_text = make_text(chain_dict)

# print random_text
