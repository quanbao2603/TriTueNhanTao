import collections

def depth_first_search(visited, graph, root, target):
    if root not in visited:
        print(root, end=" ") 
        visited.add(root)
        
        if root == target:
            return True  
        
        for neighbour in graph[root]:
            if depth_first_search(visited, graph, neighbour, target):
                return True  

    return False 

if __name__ == "__main__":
    graph = {
        1: [2, 6, 5, 7, 11], 2: [1, 6, 8, 11], 3: [4, 8, 9, 10, 11], 
        4: [3, 9], 5: [1, 7], 6: [1, 2], 7: [1, 5], 8: [2, 3], 9: [3, 4], 10: [3], 11: [1, 2, 3]
    }
    
    root = int(input("Nhập đỉnh bắt đầu: "))  
    if root not in graph:
        print("Đỉnh không hợp lệ!")
        exit()
    
    print(f"Bắt đầu từ đỉnh {root}, tìm đến đỉnh 1 theo DFS:")
    visited = set()
    depth_first_search(visited, graph, root, 1) 
