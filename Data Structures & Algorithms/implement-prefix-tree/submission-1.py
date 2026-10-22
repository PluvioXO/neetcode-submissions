class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        current = self.root
        ptr = 0 
        while ptr < len(word): 
            if word[ptr] not in current:
                current[word[ptr]] = {} 
            current = current[word[ptr]]
            ptr += 1 
        current["*"] = {} 

    def search(self, word: str) -> bool:
        current = self.root
        ptr = 0 
        while ptr < len(word): 
            if word[ptr] not in current:
                return False; 
            current = current[word[ptr]]
            ptr += 1 
        if "*" in current:
            return True; 
        return False 

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        ptr = 0 
        while ptr < len(prefix):
            if prefix[ptr] not in current:
                return False
            current = current[prefix[ptr]]
            ptr += 1 
        if len(current) > 0:
            return True
        return False
        