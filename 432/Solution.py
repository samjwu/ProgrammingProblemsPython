class Node:
    def __init__(self, freq: int):
        self.freq = freq
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.keyToNode = {}

    def inc(self, key: str) -> None:
        if key in self.keyToNode:
            # if node for key exists, get node and its freq
            node = self.keyToNode[key]
            freq = node.freq

            # then assign key to node with freq + 1
            node.keys.remove(key)
            nextNode = node.next

            # create the node if it does not exist
            if nextNode == self.tail or nextNode.freq != freq + 1:
                newNode = Node(freq + 1)
                newNode.keys.add(key)

                node.next = newNode
                newNode.prev = node

                newNode.next = nextNode
                nextNode.prev = newNode

                self.keyToNode[key] = newNode
            else:
                nextNode.keys.add(key)

                self.keyToNode[key] = nextNode

            # delete node if it has no keys
            if not node.keys:
                self.removeNode(node)
        else:
            # if node for key does not exist, create it
            node = self.head.next
            if node == self.tail or node.freq > 1:
                newNode = Node(1)
                newNode.keys.add(key)

                self.head.next = newNode
                newNode.prev = self.head

                newNode.next = node
                node.prev = newNode

                self.keyToNode[key] = newNode
            else:
                node.keys.add(key)

                self.keyToNode[key] = node

    def dec(self, key: str) -> None:
        # early exit if key does not exist
        if key not in self.keyToNode:
            return

        # remove key from node
        node = self.keyToNode[key]
        node.keys.remove(key)

        # update the key to node map
        freq = node.freq
        if freq == 1:
            # if freq was 1, key can be deleted from map
            del self.keyToNode[key]
        else:
            # otherwise move key to node with freq - 1
            prevNode = node.prev

            # create the node if it does not exist
            if prevNode == self.head or prevNode.freq != freq - 1:
                newNode = Node(freq - 1)
                newNode.keys.add(key)

                prevNode.next = newNode
                newNode.prev = prevNode

                newNode.next = node
                node.prev = newNode

                self.keyToNode[key] = newNode
            else:
                prevNode.keys.add(key)

                self.keyToNode[key] = prevNode

        # delete node if it has no keys
        if not node.keys:
            self.removeNode(node)

    def getMaxKey(self) -> str:
        # if no keys exist, return empty string
        if self.tail.prev == self.head:
            return ""

        # otherwise return any key from tail.prev node
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        # if no keys exist, return empty string
        if self.head.next == self.tail:
            return ""

        # otherwise return any key from head.next node
        return next(iter(self.head.next.keys))

    def removeNode(self, node: Node) -> None:
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode
