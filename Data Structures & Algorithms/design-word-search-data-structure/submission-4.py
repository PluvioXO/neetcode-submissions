class WordDictionary:

    def __init__(self):
        # we can solve this problem using a prefix tree 
        self.root = {}; 

    def addWord(self, word: str) -> None:
        current = self.root
        ptr = 0 
        while ptr < len(word): 
            if word[ptr] not in current:
                current[word[ptr]] = {}
            current = current[word[ptr]]
            ptr += 1 
        current["*"] = {}
        
    def __recursiveSearch(self, current : dict, word: str, ptr: int) -> bool: 
        #print(ptr, word)
        # we take in the current dict in the tree we are traversing, then we look at the currentStr po
        while ptr < len(word): 
            if word[ptr] == ".": 
                # iterate throug the available keys of current
                for key in list(current.keys()):
                    if self.__recursiveSearch(current[key], word, ptr+1): 
                        return True
                return False
                # produces an array of booleans e.g: [True, False, False ....] and maps OR between them all. 
            elif word[ptr] not in current: 
                return False 
            else: 
                current = current[word[ptr]]
            ptr += 1 
        if "*" not in current:
            return False
        return True

    def search(self, word: str) -> bool:
        current = self.root
        #print(current)
        ptr = 0 
        while ptr < len(word): 
            if word[ptr] == ".": 
                if len(current) < 1: 
                    return False
                # iterate throug the available keys of current
                for key in list(current.keys()):
                    if self.__recursiveSearch(current[key], word, ptr+1): 
                        return True
                return False
                # produces an array of booleans e.g: [True, False, False ....] and maps OR between them all. 
            elif word[ptr] not in current: 
                return False 
            else: 
                current = current[word[ptr]]
            ptr += 1 
        if "*" not in current:
            return False 
        return True