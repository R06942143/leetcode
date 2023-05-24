class Node:
    def __init__(self, key: int, value: int, prev=None, next=None):
        self.prev = prev
        self.next = next
        self.key = key
        self.value = value


class DoubleLinkedList:
    def __init__(self):
        self.head = Node(0, 0)  # create a dummy node
        self.tail = Node(0, 0)
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def get_size(self) -> int:
        return self.size

    def add(self, newNode: Node) -> None:
        tmp = self.head.next
        self.head.next = newNode
        newNode.prev = self.head
        newNode.next = tmp
        tmp.prev = newNode
        self.size += 1

    def remove(self, node: Node) -> None:
        prevNode = node.prev
        nextNode = node.next
        if prevNode and nextNode:
            prevNode.next = nextNode
            nextNode.prev = prevNode
            self.size -= 1
            node.next = None
            node.prev = None
        else:
            # TODO raise error
            pass

    def removeLeastSeenNode(self) -> Node | None:
        if self.size == 0:
            return None
        removeNode = self.tail.prev
        removeNode.prev.next = self.tail
        self.tail.prev = removeNode.prev
        self.size -= 1
        removeNode.next = None
        removeNode.prev = None
        return removeNode


class LRUCache:
    def __init__(self, capacity: int):
        self.map = {}
        self.cache = DoubleLinkedList()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.map:
            self.cache.remove(self.map[key])
            self.cache.add(self.map[key])
            return self.map[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        newNode = Node(key=key, value=value)
        if key in self.map:
            self.cache.remove(self.map[key])
            self.cache.add(newNode)
            self.map[key] = newNode
        else:
            if self.cache.get_size() == self.capacity:
                removeNode = self.cache.removeLeastSeenNode()
                if removeNode:
                    del self.map[removeNode.key]
            self.cache.add(newNode)
            self.map[key] = newNode


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
