class Node:
    def __init__(self, key, value, next_node = None):
        self.key = key
        self.value = value
        self.next = next_node


class MyHashMap:

    def __init__(self):
        self.array_length = 100000
        self.map = [None] * self.array_length

    def put(self, key: int, value: int) -> None:
        hash_key = hash(key) % self.array_length
        if not self.map[hash_key]:
            self.map[hash_key] = Node(key, value)
            return
        else:
            current_node = self.map[hash_key]
            while current_node:
                if current_node.key == key:
                    current_node.value = value
                    return
                if not current_node.next:
                    current_node.next = Node(key, value)
                    return
                current_node = current_node.next
            return 

    def get(self, key: int) -> int:
        hash_key = hash(key) % self.array_length
        current_node = self.map[hash_key]
        while current_node:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next
        return -1


    def remove(self, key: int) -> None:
        hash_key = hash(key) % self.array_length
        current_node = self.map[hash_key]
        if not current_node:
            return
        prev = dummpy_node = Node(0, 0, current_node)
        now = prev.next
        while now:
            if now.key == key:
                prev.next = now.next
                now.next = None
                self.map[hash_key] = dummpy_node.next
                return
            now = now.next
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)