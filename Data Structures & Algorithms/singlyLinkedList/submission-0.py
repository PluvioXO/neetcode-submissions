class LinkedList:
    
    def __init__(self):
        # Default list node init. 
        self.Nodelist = [] 
    
    def get(self, index: int) -> int:
        if index < len(self.Nodelist):
            return self.Nodelist[index]
        return -1

    def insertHead(self, val: int) -> None:
        self.Nodelist.insert(0, val)

    def insertTail(self, val: int) -> None:
        self.Nodelist.append(val)

    def remove(self, index: int) -> bool:
        if index >= len(self.Nodelist):
            return False 
        self.Nodelist.pop(index)
        return True
        

    def getValues(self) -> List[int]:
        return self.Nodelist
