from nlmetrics import *
from nlmodels import *

def similarity(s1, s2, metrics, model):

    ld = levenshtein_distance(s1, s2)
    hd = hamming_distance(s1, s2)
    ji = jaccard_index(s1, s2)

    # bow = Bag-of-words
    if model == "bow":
        vec1, vec2 = bag_of_words(s1, s2)
        dot_product = sum([vec1[i] * vec2[i] for i in range(len(vec1))])
        if metrics == "jaccard":
            similarity = ji + dot_product / (len(vec1) * len(vec2))
        elif metrics == "levenshtein":
            similarity = 1 - ld / max(len(s1), len(s2)) + dot_product / (len(vec1) * len(vec2))
        else:
            if hd != None:
                similarity = 1 - hd / max(len(s1), len(s2)) + dot_product / (len(vec1) * len(vec2))
            else:
                similarity = "Can't calculate Hamming distance because two strings are not in the same length"

    elif model == "tfidf":
        similarity = 0
        dict, words, w = tfidf(s1, s2)
        for word in words:
            if word in dict and w[0] > 0 and w[1] > 0:
                if metrics == "jaccard":
                    similarity += w[0] * w[1] * jaccard_index(s1.replace(word, ''), s2.replace(word, ''))
                elif metrics == "levenshtein":
                    similarity += w[0] * w[1] * (1 / (1+levenshtein_distance(word, word)))
                else:
                    if hd != None:
                        similarity += w[0] * w[1] * (1 / (1+hamming_distance(word, word)))
                    else:
                        similarity = "Can't calculate Hamming distance because two strings are not in the same length"

    else:
        if metrics == "jaccard":
            similarity = ji * cosine(s1, s2)
        elif metrics == "levenshtein":
            similarity = 1 / (1 + ld) * cosine(s1, s2)
        else:
            if hd != None:
                similarity = 1 / (1 + hd) * cosine(s1, s2)
            else:
                similarity = "Can't calculate Hamming distance because two strings are not in the same length"
    if type(similarity) != str:
        similarity = round(similarity, 3)
    return similarity

