def levenshtein_distance(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    return dp[m][n]

def hamming_distance(s1, s2):
    if (len(s1) == len(s2)):
        return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def jaccard_index(s1, s2):
    words1 = set(s1.split())
    words2 = set(s2.split())
    intersection = len(words1 & words2)
    union = len(words1 | words2)
    return intersection / union