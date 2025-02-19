class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # 3 possible chars to append: abc
        # string of length n

        # first spot has 3 choices
        # remaining n-1 spots have 2 choices (since no repeats allowed)
        # therefore 3 * 2^(n-1) total possibilities
        total = 3 * (1 << (n-1))

        if k > total:
            return ""

        ans = ["a"] * n

        # map each char to its next smallest and next greatest
        next_smallest = {
            "a": "b",
            "b": "a",
            "c": "a"
        }
        next_greatest = {
            "a": "c",
            "b": "c",
            "c": "b"
        }

        # index of first string starting with a is 1
        start_a = 1
        # index of first string starting with b is after all strings starting with a
        # there are 2^(n-1) strings starting with a
        start_b = start_a + (1 << (n-1))
        # index of first string starting with c is after all strings starting with b
        # there are 2^(n-1) strings starting with b
        start_c = start_b + (1 << (n-1))

        # compare each range to k to determine starting char
        if k < start_b:
            ans[0] = "a"
            k -= start_a
        elif k < start_c:
            ans[0] = "b"
            k -= start_b
        else:
            ans[0] = "c"
            k -= start_c

        # fill in remainder of answer
        for i in range(1, n):
            # for each remainder, there are only two choices (since no repeats allowed)
            # since the ith char has already been selected,
            # there are 2^(n-1 - i) remaining possibilties
            midpoint = 1 << (n-1 - i)

            # compare each range to k to determine next char
            if k < midpoint:
                ans[i] = next_smallest[ans[i - 1]]
            else:
                ans[i] = next_greatest[ans[i - 1]]
                k -= midpoint

        return "".join(ans)
