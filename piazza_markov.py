import re
import random

# Function for markov chain walking.. inefficient, but only 25k words so no prob

def markov_pred(words,size,n_grams=3):
    """Markov chain to do simplistic text walking.
    ---------
    Args: 
        words; list with all the words in the text corpus.  The assumption
            is that this list is NOT unique and is in the order that it
            was originally found in.
            
        size; int, how far you want to walk down the markov chain.
          
        n_grams: how many words are used before a predicted word to calculate
            the probability of that predicted word occuring.
    ---------
    Returns: 
        a string that is the walk of length 'size' down the chain.
    """
    # create a word bank of n-grams
    gram_bank = []
    for i in range(len(words)-n_grams-1):
        gram_bank.append(tuple(words[i:i+n_grams]))
    
    # create the dictionary with a list of the words following each n-gram
    word_dict = {}
    for ngram in gram_bank:
        key = tuple(ngram[:-1])
        if key in word_dict:
            word_dict[key].append(ngram[-1])
        else:
            word_dict[key] = [ngram[-1]]
            
    # walk through the dictionary based on the probability of successive words
    seed = random.randint(0, len(words)-n_grams)
    current = words[seed:seed+n_grams-1]
    gen_words = []
    for i in range(size):
        gen_words.append(current[0])
        new_word = random.choice(word_dict[tuple(current)])
        current.pop(0)
        current.append(new_word)
        #gen_words.append(current[0])
    
    return ' '.join(gen_words)

###############################################################
    
if __name__=='__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Walk the Markov chain of 209 Piazza posts.')
    parser.add_argument('-l', \
            help='This flag specifies the length of the text output you get. Defaults to 100')
    parser.add_argument('-g', \
            help='This flag specifies the length of the n-grams you use in the chain. Default is 5.')
    args = parser.parse_args()
    
    # Defaults
    length = 100
    n_grams = 5
    
    # If flags are active change defaults
    if args.l:
        try:
            length = int(args.l)
        except:
            raise ValueError('please pass an integer')
    
    if args.g:
        try:  
            n_grams = int(args.g)
        except:
            raise ValueError('please pass an integer')

    # Import the text file
    with open('piazza_posts.txt', 'r') as file:
        posts = file.read()
    
    clean = re.sub('<[^>]+>', '', posts)
    words = clean.split()
    
    # Print out results
    print(markov_pred(words,length,n_grams))


