from typing import List

class Solution:
    def removeSubfolders(self, paths: List[str]) -> List[str]:
        top_folders = []
        
        path_set = set(paths)

        for path in paths:
            # create copy to modify
            temp_path = path
            is_subfolder = False
            
            # continue moving up path until reach the root
            while not temp_path == "":
                last_slash_idx = temp_path.rfind("/")

                # reached root
                if last_slash_idx == -1:
                    break

                # extract parent folder
                temp_path = temp_path[0:last_slash_idx]

                # check if parent folder already exists
                if temp_path in path_set:
                    is_subfolder = True
                    break

            if not is_subfolder:
                top_folders.append(path)

        return top_folders
