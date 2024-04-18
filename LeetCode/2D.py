def longest_common_subsequence(X, Y):
    m = len(X)
    n = len(Y)

    # Create a 2D table to store the lengths of LCSs
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the dp table in a bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Retrieve the longest common subsequence
    lcs = ""
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs = X[i - 1] + lcs
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return lcs

# Example usage
X = "AGGTAB"
Y = "GXTAYB"
print("Longest Common Subsequence:", longest_common_subsequence(X, Y))
