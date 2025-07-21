class Solution:
    def makeFancyString(self, s: str) -> str:
        chars = []
        prev_char = ""
        same_char_count = 1

        for c in s:
            if prev_char == c:
                same_char_count += 1
                
                if same_char_count > 2:
                    continue
            else:
                same_char_count = 1

            prev_char = c
            chars.append(c)

        return "".join(chars)
