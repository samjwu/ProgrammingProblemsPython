class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}

class Solution:
    def removeSubfolders(self, paths: List[str]) -> List[str]:
        root = TrieNode()

        for path in paths:
            currNode = root
            folders = path.split("/")

            for folder in folders:
                if folder == "":
                    continue

                if folder not in currNode.children:
                    currNode.children[folder] = TrieNode()
                    
                currNode = currNode.children[folder]

            currNode.isEnd = True

        result = []

        for path in paths:
            currNode = root
            folders = path.split("/")
            isSubfolder = False

            for i, folder in enumerate(folders):
                if folder == "":
                    continue

                nextNode = currNode.children[folder]
                
                if nextNode.isEnd and i != len(folders) - 1:
                    isSubfolder = True
                    break
                
                currNode = nextNode

            if not isSubfolder:
                result.append(path)

        return result
