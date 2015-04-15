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
        if index == len(word_list) - 2:
            break
        third_word = word_list[index + 2]

        bigrams.setdefault((current_word, second_word), [])
        bigrams[current_word, second_word].append(third_word)
        # the code below does the same thing:
        # if (current_word, second_word) not in bigrams:
        #     bigrams[current_word, second_word] = []
        #     bigrams[current_word, second_word].append(third_word)

        # else: 
        #     bigrams[current_word, second_word].append(third_word)

    return bigrams

def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
# Randomly choose tuple from bigram dictionary ex. (a, box) : [for, for, in, house]
# Add word pair to string "a box"
# Choose random word from value list of the tuple (pretend it chooses 'for')
# Add the random word from the value list to string "a box for"
## while loop starts here
# Make new tuple of second word ("box") and the random word ("for") (box, for)
# Check to see if the newly made tuple is in dictionary.  Pretend it is 
# (box, for): [house, mouse]
# If it is then choose random word (pretend it's "house) from value list and add 
# that to string which is now "a box for house"
## while loop ends here
    import random
    
    rand_key = random.choice(chains.keys())
    # another way to do this:
    # bigrams_list = chains.keys()
    # rand_num = random.randint(0, len(bigrams_list) - 1)
    # rand_key = bigrams_list[rand_num]
    
    rand_value_word = random.choice(chains[rand_key])
    # you can also do this by generating a random number using random.randint and then 
    # use that number as the index to retrieve a key from a list of chains.keys()

    key1, key2 = rand_key
    markov_string = key1 + " " + key2 + " " + rand_value_word
    
    while rand_key in chains:
        
        new_bigram = tuple([key2, rand_value_word])
        if new_bigram in chains:
            rand_new_word = random.choice(chains[new_bigram])
            markov_string += " " + rand_new_word
            key2 = rand_value_word
            rand_value_word = rand_new_word            
        else:
            markov_string += "."
            return markov_string

        
print(make_text(make_chains()))
# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

input_text = "Some textSome textSome textSome textSome textSome textSome textSome textSome textSome textSome textSome textSome textSome text"

# Get a Markov chain
#chain_dict = make_chains(input_text)

# Produce random text
# random_text = make_text(chain_dict)

# print random_text
