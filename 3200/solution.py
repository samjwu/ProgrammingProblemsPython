class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def simulate_height(type_1: int, type_2: int) -> int:
            height = 0
            row_number = 1

            while True:
                if row_number % 2 == 1:
                    if type_1 >= row_number:
                        type_1 -= row_number
                    else:
                        break
                else:
                    if type_2 >= row_number:
                        type_2 -= row_number
                    else:
                        break

                row_number += 1
                height += 1

            return height

        # try both cases: red as row 1 and blue as row 1
        return max(simulate_height(red, blue), simulate_height(blue, red))
