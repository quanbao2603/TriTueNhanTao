def depth_limited_search(graph, node, target, visited, depth, limit):
    if depth > limit:
        return False  
    
    if node not in visited:
        print(node, end=" ")
        visited.add(node)

        if node == target:
            return True  
        for neighbor in graph.get(node, []):
            if depth_limited_search(graph, neighbor, target, visited, depth + 1, limit):
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

    limit = int(input("Nhập độ sâu tối đa: "))

    print(f"Bắt đầu từ đỉnh {root}, tìm đến đỉnh 1 với giới hạn {limit}:")
    visited = set()
    
    found = depth_limited_search(graph, root, 1, visited, 0, limit)
    
    print("\nTìm thấy đỉnh 1!" if found else "\nKhông tìm thấy trong giới hạn độ sâu!")
