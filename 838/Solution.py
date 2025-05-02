class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        ans = list(dominoes)

        # key positions are LR dominoes
        # add a L and R to each end, to make edge cases easier
        # eg: ..R..
        key_positions = [(-1, 'L')]
        for index, symbol in enumerate(dominoes):
            if symbol != '.':
                key_positions.append((index, symbol))
        key_positions.append((n, 'R'))

        def compare(a, b):
            if a < b:
                return -1
            elif a > b:
                return 1
            else:
                return 0

        # process pairs of key dominoes
        for (left_index, left_symbol), (right_index, right_symbol) in zip(key_positions, key_positions[1:]):
            # same direction (R...R, L...L)
            # everything in between falls in same direction
            if left_symbol == right_symbol:
                for k in range(left_index + 1, right_index):
                    ans[k] = left_symbol

            # towards each other (R...L)
            # everything in between falls same direction as the closer one
            elif left_symbol == 'R' and right_symbol == 'L':
                for k in range(left_index + 1, right_index):
                    dist_from_left = k - left_index
                    dist_from_right = right_index - k
                    comparison = compare(dist_from_left, dist_from_right)

                    if comparison < 0:
                        ans[k] = 'R'
                    elif comparison > 0:
                        ans[k] = 'L'
                    else:
                        ans[k] = '.'

            # away from each other (L...R)
            # everything in between is unchanged. ignore this case

        return ''.join(ans)
