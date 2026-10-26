class TimeMap:
    def __init__(self):
        self.record = {} 
        self.timestamps = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if timestamp not in self.record:
            self.record[timestamp] = {}
        self.record[timestamp][key] = value
        # also store the available timestamps options for later 

        if key not in self.timestamps:
            self.timestamps[key] = []
        self.timestamps[key].append(timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if timestamp in self.record and key in self.record[timestamp]:
            return self.record[timestamp][key]
        if key not in self.timestamps:
            return "" 
        ptr = len(self.timestamps[key])-1
        while ptr > -1: 
            if self.timestamps[key][ptr] <= timestamp:
                correctTimestamp = self.timestamps[key][ptr]
                return self.record[correctTimestamp][key]
            ptr -= 1 
        return ""
