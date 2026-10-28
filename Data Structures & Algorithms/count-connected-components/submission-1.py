class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {} 
        for item in edges: 
            start, end = item
            if start not in graph: 
                graph[start] = [] 
            if end not in graph: 
                graph[end] = [] 
            
            graph[start].append(end)
            graph[end].append(start)
        
        seen = set()
        total = 0 
        def search(key: int):
            nonlocal seen; 
            if key in seen:
                return; 
            seen.add(key)
            [search(nextKey) for nextKey in graph[key]]

        for key in list(graph.keys()):
            if key not in seen:
                search(key)
                total += 1 
            if len(graph) == len(seen):
                return total + (n - len(seen)); 