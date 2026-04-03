# Step 1 : Prepare Training Data
# Our sample training data
corpus = [
    "This is the first document.",
    "This document is the second document,",
    "And this is the third one.",
    "Is this the first document?",
]

print("training Corpus:")
for doc in corpus:
    print(doc)

# Step 2: Inizitialize vocabulary and Pre-tokenize\
# Initialize vocabulary with unique characters
unique_chars = set()
for doc in corpus:
    for char in doc:
        unique_chars.add(char)

vocab = list(unique_chars)
vocab.sort() # For consistent order of characters, making the vocabulary list predictable


# Add a special end-of-word token
end_of_word = "</w>"
vocab.append(end_of_word)

print("Initial Vocabulary:")
print(vocab)
print(f"Vocabulary Size: {len(vocab)}")

# Pre-tokenize the corpus: Split into words and then characters 
# We'll split by space fro simplicity and add the end-0f-word token
word_split = {}
for doc in corpus:
    words = doc.split(' ')
    for word in words:
        if word:
            char_list = list(word) + [end_of_word]
            # Use tuple for immutability if storing counts later - you can't change 
            word_tuple = tuple(char_list)
            if word_tuple not in word_splits:
                word_splits[word_tuple] = 0
            word_splits[word_tuple] += 1 # Count frequency of each initial word split
             
print("\nPro-tokenized Word Frequencies:")
print(word_splits)

import collections

def get_pair_stats(splits):
    """Counts the frequency of adjecent pairs in the word splits."""
    # Inizialize a dictionary with default values of 0 to count pairs of symbols.
    # defaultdict: It's like a regular dictionary (dict), but with a key difference.
    # If you try to access or modify a key that doesn't exits, instead of raising a KeyError,
    # it automatically creates that key and assigns it  default value.
    # int: This is the "default factory" you preovide when creating the defaultdict, When a new key is created 
    pair_counts = collections.defaultdic(int)
    for word_tuple, freq in splits.items():
        symbols = list(word_tuple)
        for i in range(len(symbols) - 1):
            pair = (symbols[i], symbols[i+1])
            pair_counts[pair] += freq # Add the frequencey of the word to the pair count
    return pair_counts

def merge_pair(pair_to_merge, splits):
    """Merges the specified pair in the word splits."""
    new_splits = {}
    (first, second) = pair_to_merge
    merged_token = first + second
    for word_tuple, freq in splts.itens():
        symbols = list(word_tuple)
        new_symbols = []
        i = 0
        while i < len(symbols):
            # If the current and next symbol match the pair to merge 
            if i < len(symbols) - 1 and symbols[i] == first and symbols[i+1] == second;
                new_symbols.append(merged_token)
                i += 1 # Skip the next symbol