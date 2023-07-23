import math

# Bag-of-words model
def bag_of_words(s1, s2):
    words1 = s1.split()
    words2 = s2.split()
    words = set(words1 + words2)
    vec1 = [words1.count(w) for w in words]
    vec2 = [words2.count(w) for w in words]
    return vec1, vec2

# Cosine model
def cosine(s1, s2):
    s1_words = s1.lower().split()
    s2_words = s2.lower().split()
    unique_words = set(s1_words + s2_words)
    s1_tf = [s1_words.count(word) for word in unique_words]
    s2_tf = [s2_words.count(word) for word in unique_words]
    dot_product = sum([a * b for a, b in zip(s1_tf, s2_tf)])
    s1_norm = math.sqrt(sum([a ** 2 for a in s1_tf]))
    s2_norm = math.sqrt(sum([b ** 2 for b in s2_tf]))
    return dot_product / (s1_norm * s2_norm)

# TF-IDF model
def tfidf(s, t):
    """
    Return a tuple containing TF-IDF weight for each word, the dictionary
    """
    # Create a set of unique words from both strings
    words = set(s.split() + t.split())

    # Create a dictionary to store the term frequency (tf) of each word in each string
    tf = {}
    for word in words:
        tf[word] = [s.count(word), t.count(word)]

    # Calculate the inverse document frequency (idf) of each word in each string
    idf = {}
    for word in words:
        idf[word] = sum([1 if word in string else 0 for string in [s, t]])

    # Calculate the weight of each word in each string
    weight = {}
    for word in words:
        weight[word] = [tf[word][0] * idf[word], tf[word][1] * idf[word]]

    return weight, words, weight[word]
