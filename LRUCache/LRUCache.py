class LRUCache:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.data: dict[int, list[int]] = {}
        self.recents: list[int] = []

    def get(self, key: int) -> int:
        result = -1

        if key in self.data:
            result = self.data[key][0]
            index_to_move = self.data[key][1]
            del self.recents[index_to_move]
            self.recents.append(key)
            self.data[key] = [result, len(self.recents) - 1]

        return result

    def put(self, key: int, value: int) -> None:
        if len(self.recents) == self.capacity:
            key_to_delete = self.recents.pop(0)
            del self.data[key_to_delete]

        self.data[key] = [value, len(self.recents)]
        self.recents.append(key)


obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
param_1 = obj.get(1)
obj.put(3, 3)
param_2 = obj.get(1)
obj.put(4, 4)
param_3 = obj.get(1)
print(obj.data)
print(obj.recents)
