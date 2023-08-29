def canFinish(tasks, prerequisites):
    # Create an adjacency list representation of the graph
    graph = [[] for _ in range(tasks)]
    in_degree = [0] * tasks
    
    # Populate the adjacency list and in-degree array
    for prereq in prerequisites:
        course, prereq_course = prereq
        graph[prereq_course].append(course)
        in_degree[course] += 1
    
    # Initialize a queue with courses having no prerequisites
    queue = []
    for course in range(tasks):
        if in_degree[course] == 0:
            queue.append(course)
    
    # Perform topological sorting
    while queue:
        course = queue.pop(0)
        for next_course in graph[course]:
            in_degree[next_course] -= 1
            if in_degree[next_course] == 0:
                queue.append(next_course)
    
    # If all courses are taken (no cycles), return True; otherwise, return False
    return sum(in_degree) == 0

# Test cases
print(canFinish(2, [[0, 1], [1, 0]]))  # Output: False
print(canFinish(3, [[1, 0], [0, 2]]))  # Output: True
