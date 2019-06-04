"""
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
"""


def isRegexMatch(s, p):
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
                if j < n-1 and p[j+1] == "*":
                    match_one, match_none = False, False
                    # No match
                    match_none = dp[i][j+2]
                    # 1 char match
                    if i < m:
                        if s[i] == p[j] or p[j] == ".":
                            match_one = dp[i+1][j]

                    dp[i][j] = match_none or match_one
                else:
                    if i < m:
                        if s[i] == p[j] or p[j] == ".":
                            dp[i][j] = dp[i+1][j+1]

    return dp[0][0]

if __name__ == "__main__":
    strings = ["aa", "aa", "ab", "aab", "mississippi"]
    prefixes = ["a", "a*", ".*", "c*a*b", "mis*is*p*"]

    for i in range(len(strings)):
        print("string: {}; prefix: {}; IsMatch: {}".format(strings[i],
                                                           prefixes[i],
                                                           isRegexMatch(strings[i], prefixes[i])))



