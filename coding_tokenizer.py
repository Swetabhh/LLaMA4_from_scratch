<<<<<<< HEAD
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
            else:
                new_symbols.append(symbols[i])
                i += 1
        new_splits[tuple(new_symbols)] = freq # Use the updated symbol list as the key
    return new_splits

# Step 3: Iterative BPE Merging Loop
num_merges = 15
merges = {} 

current_splits = word_splits.copy() # Start with initial word splits

print("\n--- Startiung BPE Merges ---")
print(f"Initial Splits: {current_splits}")
print("-" * 30)

for i in range(num_merges):
    print(f"\nMerge Iteration {i+1}/{num_merges}")

    # 1. Calculate Pair Frequencies
    pair_stats = get_pair_stats(current_splits)
    if not pair_stats:
        print("No more pairs to merge.")
        break
    # Optional: Print top 5 pairs of inspection
    sorted_pairs = sorted(pair_stats.items(), key=lambda iten: item[1], reverse=True)
    print(f"Top 5 Pair Frequencies: {sorted_pairs[:5]}")

    # 2. Find Best Pair
    best_pair = max(pair_stats, key=pair_stats.get)
    best_freq = pair_stats[best_pair]
    print(f"Found Best Pair: {best_freq}")

    # 3. Merge the Best Pair
    current_splits = merge_pair(best_pair, current_splits)
    new_token = best_pair[0] + best_pair[1]
    print(f"Merging {best_pair} into '{new_token}'")
    print(f"Splits after merges: {current_splits}")

    # 4. Update Vocabulary
    vocab.append(new_token)
    print(f"Updated Vocabulary: {vocab}") 

    # 5. Store Merge Rule
    merges[best_pair] = new_token
    print(f"Updated Merges: {merges}")

    print("-" * 30)

    # 4: Review Final Results
    # After the loop finishes,we can examine the final state:
    print("\n --- BPE Merges Complete ---")
    print(f"Final Vocabulary Size: {len(vocab)}")
    print("\nLearned Merges (Pair -> New Token):")
    # Pretty print merges
    for pair, token in merges.items():
        print(f"{pair} -> '{token}'")

    print("\nFinal Word Splits after all merges:")
    print(current_splits)

    print("\nFinal Vocabulary :")
    # Sort for consistent viewing
    final_vocab_sorted = sorted(list(set(vocab))) # Use set to remove potential duplicates if any step introduced them
print(final_vocab_sorted)



=======
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

