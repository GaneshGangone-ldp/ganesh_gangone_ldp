def dfs(node, graph, visited, stack):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, graph, visited, stack)
    stack.append(node)

def topological_sort_dfs(num_courses, prerequisites):
    
    graph = [[] for _ in range(num_courses)]

   
    for course, prereq in prerequisites:
        graph[prereq].append(course)

   
    visited = [False] * num_courses
    stack = []

    
    for course in range(num_courses):
        if not visited[course]:
            dfs(course, graph, visited, stack)

    
    return stack[::-1]


num_courses = 6
prerequisites = [
    (1, 0),  
    (2, 1),  
    (3, 1),  
    (4, 2),  
    (5, 2)   
]
print("Training Plan:", topological_sort_dfs(num_courses,prerequisites))