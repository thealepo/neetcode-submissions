from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.dictionary = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dictionary[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        rv = ''
        values = self.dictionary[key]

        left, right = 0, len(values) - 1
        while left <= right:
            mid = left + ((right - left) // 2)

            if values[mid][1] <= timestamp:
                rv = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return rv
