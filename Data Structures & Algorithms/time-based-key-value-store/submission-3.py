class TimeMap:

    def __init__(self):
        self.store = {}  # key -> list of [timestamp, value]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.store.get(key, [])
        res = ""
        l, r = 0, len(pairs) - 1
        while l <= r:
            m = (l + r) // 2
            if pairs[m][0] <= timestamp:
                res = pairs[m][1]   # valid candidate; try to find a later one
                l = m + 1
            else:
                r = m - 1
        return res