import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [(0, start)]
    while queue:
        dist, node = heapq.heappop(queue)
        if dist > distances[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(queue, (new_dist, neighbor))
    return distances

"""
|
|
|
"""

def shortest_path(graph, start, end):
    distances = dijkstra(graph, start)
    path = [end]
    while end != start:
        for neighbor, weight in graph[end]:
            if distances[end] - weight == distances[neighbor]:
                path.append(neighbor)
                end = neighbor
                break
    return list(reversed(path))
