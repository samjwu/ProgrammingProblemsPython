class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)

        # memo[i][j] = subanswer for str1[0:i] and str2[0:j]
        # store only the latest i-1 and i indices using prev and curr rows to save space
        # for i = 0, subanswer is prefix of str2
        prev_row = [str2[0:j] for j in range(n + 1)]

        for i in range(1, m + 1):
            # for j = 0, subanswer is prefix of str1
            curr_row = [str1[0:i]] + [None for _ in range(n)]

            for j in range(1, n + 1):
                # current char matches in both string, so pick either char
                if str1[i - 1] == str2[j - 1]:
                    curr_row[j] = prev_row[j - 1] + str1[i - 1]
                else:
                    # current chars don't match, so try picking char from both strings
                    pick_str1 = prev_row[j]
                    pick_str2 = curr_row[j - 1]

                    # memoize shortest of the two as subanswer
                    if len(pick_str1) < len(pick_str2):
                        curr_row[j] = pick_str1 + str1[i - 1]
                    else:
                        curr_row[j] = pick_str2 + str2[j - 1]
                    
            prev_row = curr_row

        return prev_row[n]
