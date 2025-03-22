import collections

def breadth_first_search(graph, root, target):
    visited = set()
    queue = collections.deque([root])
    visited.add(root)  
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")  
        for i in graph[vertex]:
            if i not in visited:
                queue.append(i)
                visited.add(i)  

if __name__ == "__main__":
    graph = {
        1: [2, 6, 5, 7, 11], 2: [1, 6, 8, 11], 3: [4, 8, 9, 10, 11], 
        4: [3, 9], 5: [1, 7], 6: [1, 2], 7: [1, 5], 8: [2, 3], 9: [3, 4], 10: [3], 11: [1, 2, 3]}
    
    root = int(input("Nhập đỉnh bắt đầu: "))  
    if root not in graph:
        print("Đỉnh không hợp lệ!")
        exit()
    else:
        print(f"Bắt đầu từ đỉnh {root}, tìm đến đỉnh 1:")
        breadth_first_search(graph, root, 1)
    
