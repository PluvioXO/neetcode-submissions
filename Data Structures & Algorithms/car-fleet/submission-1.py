class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        def time(x, target): 
            return (target - x[0])/x[1]
        
        if len(position) < 2: 
            return 1
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        cars.sort(key=lambda x: x[0])
        convoy = 1 
        l, r = len(cars)-2, len(cars)-1
        print(cars)
        while l >= 0:
            # Test is item 
            if time(cars[l], target) > time(cars[r], target):
                r = l 
                convoy += 1 
            l-=1
    
        return convoy 