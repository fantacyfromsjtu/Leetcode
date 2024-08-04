from typing import List
import heapq

class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def dijkstra(start: int, graph: List[List[List[int]]]) -> List[int]:
            distances = [float('inf')] * n
            distances[start] = 0
            pq = [(0, start)]
            while pq:
                current_distance, current_node = heapq.heappop(pq)
                if current_distance > distances[current_node]:
                    continue
                for neighbor, weight in graph[current_node]:
                    distance = current_distance + weight
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(pq, (distance, neighbor))
            return distances
        
        # Initialize the graph with the initial roads
        graph = [[] for _ in range(n)]
        for i in range(n - 1):
            graph[i].append((i + 1, 1))
        
        answer = []
        for ui, vi in queries:
            graph[ui].append((vi, 1))
            distances = dijkstra(0, graph)
            answer.append(distances[n - 1])
        
        return answer

# Example usage
s = Solution()
n = 5
queries = [[2, 4], [0, 2], [0, 4]]
print(s.shortestDistanceAfterQueries(n, queries))
