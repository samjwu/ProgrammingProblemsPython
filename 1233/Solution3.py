from typing import List

class Solution:
    def removeSubfolders(self, paths: List[str]) -> List[str]:
        # sort for lexicographical order
        # to give parent/top folders before subfolders
        paths.sort()

        n = len(paths)

        # first top folder is given by sorted order
        top_folders = [paths[0]]

        for i in range(1, n):
            # create copy to modify
            prev_parent = top_folders[-1]
            # add slash to avoid mistakes
            # example: /a and /ab should not match
            prev_parent += "/"

            if not paths[i].startswith(prev_parent):
                top_folders.append(paths[i])
        
        return top_folders
