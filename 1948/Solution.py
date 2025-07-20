from collections import Counter
from typing import List


class Trie:
    """
    Represent all paths as a trie

    each folder is a child node
    serialized form: parent(child)
    """
    children: dict
    serialized: str

    def __init__(self):
        self.children = dict()
        self.serialized = ""


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Trie()

        for path in paths:
            curr = root

            for node in path:
                if node not in curr.children:
                    curr.children[node] = Trie()
                curr = curr.children[node]

        # track count of serialized paths
        # to later delete duplicated paths
        freq = Counter()

        def serialize(node: Trie) -> None:
            """
            Generate serialized form of each path

            post-order traversal with depth-first search
            to get children in brackets for serialization
            for serialized form: parent(child)
            """
            # leaf node has no child
            # therefore no serialized form
            if not node.children:
                return

            serialized_subfolders = []
            
            for subfolder, child in node.children.items():
                serialize(child)
                serialized_subfolders.append(subfolder + "(" + child.serialized + ")")

            # example input: [["a", "x"], ["a", "z"], ["b", "z"], ["b", "x"]]
            # if not sorted, would result in duplicates not being deleted since
            # a.serialized = x()z()
            # b.serialized = z()x()
            serialized_subfolders.sort()
            node.serialized = "".join(serialized_subfolders)
            freq[node.serialized] += 1

        serialize(root)

        nonduplicate_folders = []
        # create temporary variable to record paths
        temp_path = []

        def collect_nonduplicates(node: Trie) -> None:
            """
            Find all non duplicate paths

            use counter to avoid duplicated paths
            """
            if freq[node.serialized] > 1:
                return

            if temp_path:
                nonduplicate_folders.append(temp_path[:])

            for subfolder, child in node.children.items():
                temp_path.append(subfolder)
                collect_nonduplicates(child)
                # backtrack to simulate traversing paths
                temp_path.pop()

        collect_nonduplicates(root)

        return nonduplicate_folders
