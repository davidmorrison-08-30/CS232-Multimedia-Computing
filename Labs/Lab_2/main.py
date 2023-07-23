from nlmetrics import *
from nlmodels import *
from similarity import *

# user input
s1 = input("Enter the first sentence: ")
s2 = input("Enter the second sentence: ")

print("\nSimilarity between two strings is:")
print("Using Bag-of-words and Levenshtein distance: ", similarity(s1, s2, "levenshtein", "bow"))
print("Using Bag-of-words and Hamming distance: ", similarity(s1, s2, "hamming", "bow"))
print("Using Bag-of-words and Jaccard index: ", similarity(s1, s2, "jaccard", "bow"))
print("\nUsing Cosine and Levenshtein distance: ", similarity(s1, s2, "levenshtein", "cosine"))
print("Using Cosine and Hamming distance: ", similarity(s1, s2, "hamming", "cosine"))
print("Using Cosine and Jaccard index: ", similarity(s1, s2, "jaccard", "cosine"))
print("\nUsing TF-IDF and Levenshtein distance: ", similarity(s1, s2, "levenshtein", "tfidf"))
print("Using TF-IDF and Hamming distance: ", similarity(s1, s2, "hamming", "tfidf"))
print("Using TF-IDF and Jaccard index: ", similarity(s1, s2, "jaccard", "tfidf"))