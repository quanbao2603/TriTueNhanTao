import heapq

def uniform_cost_search(graph, cost, start, target):
    priority_queue = [(0, start)] 
    visited = set()
    
    while priority_queue:
        g, node = heapq.heappop(priority_queue) 
        
        if node in visited:
            continue

        print(node, end=" ")
        visited.add(node)

        if node == target:
            return g 

        for neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (g + cost.get((node, neighbor), float('inf')), neighbor))

    return float('inf') 


if __name__ == "__main__":
    graph = {
        1: [2, 6, 5, 7, 11], 2: [1, 6, 8, 11], 3: [4, 8, 9, 10, 11], 
        4: [3, 9], 5: [1, 7], 6: [1, 2], 7: [1, 5], 8: [2, 3], 9: [3, 4], 10: [3], 11: [1, 2, 3]
    }
    
    cost = {
        (1, 2): 2, (1, 6): 3, (1, 5): 5, (1, 7): 1, (1, 11): 4, 
        (2, 6): 1, (2, 8): 3, (2, 11): 2, (3, 4): 2, (3, 8): 1, 
        (3, 9): 4, (3, 10): 6, (3, 11): 5, (4, 9): 2, (5, 7): 2
    }

    root = int(input("Nhập đỉnh bắt đầu: "))  
    if root not in graph:
        print("Đỉnh không hợp lệ!")
        exit()
    
    print(f"Bắt đầu từ đỉnh {root}, tìm đến đỉnh 1 theo UCS:")
    min_cost = uniform_cost_search(graph, cost, root, 1)
    
