class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        union_find = {}

        def find(x: int) -> int:
            union_find.setdefault(x, x)

            if x != union_find[x]:
                union_find[x] = find(union_find[x])

            return union_find[x]
        
        def unify(x: int, y: int) -> None:
            parent_x = find(x)
            parent_y = find(y)

            # set parent as smallest group instead of largest
            if parent_x > parent_y:
                union_find[parent_x] = parent_y
            else:
                union_find[parent_y] = parent_x
        
        # chars at same position in s1 and s2 are in the same group
        for i in range(len(s1)):
            unify(s1[i], s2[i])
        
        # build smallest lexicographical equivalent string
        # using parent (smallest) of each group
        smallest_lex_equiv = []
        for c in baseStr:
            smallest_lex_equiv.append(find(c))
            
        return ''.join(smallest_lex_equiv)
