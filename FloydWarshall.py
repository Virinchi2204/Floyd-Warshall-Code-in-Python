def floyd_warshall(n, graph):
    matrix = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = graph[i][j]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i][j]>matrix[i][k]+matrix[k][j]:
                    matrix[i][j] = matrix[i][k]+matrix[k][j]
    
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print("\n")

vertices=int(input("Enter number of vertices: "))
graph=[]
print("Enter the edge lengths matrix row wise: \n")
for i in range(vertices):
    row=list(map(int,input().split()))
    graph.append(row)
print("\n")
floyd_warshall(vertices, graph)
