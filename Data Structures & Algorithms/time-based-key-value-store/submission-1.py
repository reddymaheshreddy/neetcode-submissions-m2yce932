class TimeMap:

    def __init__(self):
        self.timestamp={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timestamp:
            self.timestamp[key].append((value,timestamp))
        else:
            self.timestamp[key] = [(value,timestamp)]
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamp:
            return ""
        timestamps = self.timestamp[key]
        
        low = 0
        high = len(timestamps)-1
    
        while low <=high:
            mid = (low + high)//2
            if timestamps[mid][1] > timestamp:
                high = mid - 1
            elif timestamps[mid][1] == timestamp:
                return timestamps[mid][0]
            else:
                low = mid + 1
        if high >= 0:
            return timestamps[high][0]
        return ""
        
