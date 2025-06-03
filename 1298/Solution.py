import collections

class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int],
    ) -> int:
        n = len(status)

        # track which boxes we have keys for (or don't need keys for)
        has_key = [status[i] == 1 for i in range(n)]

        # track which boxes we have available
        has_box = [False] * n

        # track which boxes already opened
        opened_box = [False] * n

        q = collections.deque()
        ans = 0

        # open first boxes
        for box in initialBoxes:
            has_box[box] = True

            # open boxes we have available and do not need keys for
            if has_key[box]:
                q.append(box)
                opened_box[box] = True
                ans += candies[box]

        while len(q) > 0:
            curr_box = q.popleft()

            # check keys in current box
            for key in keys[curr_box]:
                has_key[key] = True

                # open boxes we just got keys for
                if not opened_box[key] and has_box[key]:
                    q.append(key)
                    opened_box[key] = True
                    ans += candies[key]

            # check boxes in current box
            for box in containedBoxes[curr_box]:
                has_box[box] = True

                # open boxes we just made available
                if not opened_box[box] and has_key[box]:
                    q.append(box)
                    opened_box[box] = True
                    ans += candies[box]

        return ans
