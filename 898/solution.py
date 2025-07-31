from typing import List


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # all unique bitwise OR values
        unique_ors = set()

        # all OR values seen so far
        curr_ors = {0}

        for new_num in arr:
            # generate all new OR values using the new number
            # also OR new_num with itself to account for empty set case
            curr_ors = {new_num | prev_num for prev_num in curr_ors} | {new_num}
            # add new OR values
            unique_ors |= curr_ors

        return len(unique_ors)
