class Graph:
    def __init__(self, graph):
        self.graph = graph

    def depth_limited_search(self, node, target, depth, limit, visited):
        if depth > limit:
            return False  # Đạt giới hạn độ sâu

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            if node == target:
                return True  # Tìm thấy đỉnh đích

            for neighbor in self.graph.get(node, []):
                if self.depth_limited_search(neighbor, target, depth + 1, limit, visited):
                    return True  

        return False  # Không tìm thấy trong giới hạn độ sâu

if __name__ == "__main__":
    graph_data = {
        1: [2, 6, 5, 7, 11], 2: [1, 6, 8, 11], 3: [4, 8, 9, 10, 11], 
        4: [3, 9], 5: [1, 7], 6: [1, 2], 7: [1, 5], 8: [2, 3], 9: [3, 4], 10: [3], 11: [1, 2, 3]
    }

    g = Graph(graph_data)

    root = int(input("Nhập đỉnh bắt đầu: "))  
    if root not in graph_data:
        print("Đỉnh không hợp lệ!")
        exit()

    limit = int(input("Nhập độ sâu tối đa: "))

    print(f"Bắt đầu từ đỉnh {root}, tìm đến đỉnh 1 với giới hạn {limit}:")
    visited = set()
    
    found = g.depth_limited_search(root, 1, 0, limit, visited)
    
    print("\nTìm thấy đỉnh 1!" if found else "\nKhông tìm thấy trong giới hạn độ sâu!")
