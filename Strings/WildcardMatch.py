"""

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
"""
def isMatch(s, p):
    m = len(s)
    n = len(p)

    dp = [[False for j in range(n+1)] for i in range(m+1)]

    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            if i == m and j == n:
                dp[i][j] = True
            elif i < m and j == n:
                dp[i][j] = False
            else:
                if p[j] == "*":
                    match_any, match_empty = False, False
                    # Match any
                    if i < m:
                        match_any = dp[i+1][j]
                    # Match empty
                    match_empty = dp[i][j+1]
                    dp[i][j] = match_any or match_empty
                else:
                    if i < m:
                        if s[i] == p[j] or p[j] == '?':
                            dp[i][j] = dp[i+1][j+1]
                        else:
                            dp[i][j] = False
    return dp[0][0]

if __name__ == "__main__":
    strings = ["aa", "aa", "cb", "adceb", "acdcb"]
    prefixes = ["a", "*", "?a", "*a*b", "a*c?b"]

    for i in range(len(strings)):
        print("string: {}; prefix: {}; IsMatch: {}".format(strings[i],
                                                           prefixes[i],
                                                           isMatch(strings[i], prefixes[i])))
