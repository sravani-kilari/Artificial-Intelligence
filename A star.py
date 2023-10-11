import copy


initial_state = [[2, 8, 3], [1, 6, 4], [7, 0, 5]] 
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  
n = 2
g = 0

def print_graph(graph):
    for row in graph:
        for col in row:
            print(col, end=" ")
        print()

def up(graph, row_index, col_index):
    if row_index - 1 >= 0:
        return True
    return False

def down(graph, row_index, col_index):
    if row_index + 1 <= n:
        return True
    return False

def left(graph, row_index, col_index):
    if col_index - 1 >= 0:
        return True
    return False

def right(graph, row_index, col_index):
    if col_index + 1 <= n:
        return True
    return False

def find_row_index(matrix, val):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == val:
                return i
    return -1

def find_col_index(matrix, val):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == val:
                return j
    return -1

def is_goal_state(graph):
    return graph == goal_state  
def find_heu(graph):
    hs = -1
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            row = find_row_index(goal_state, graph[i][j])
            col = find_col_index(goal_state, graph[i][j])
            hs += abs(row - i) + abs(col - j)
    
    return hs

def find_least_hs(queue):
    hs = 500
    g = 0
    for q in queue:
        if find_heu(q) <= hs:
            hs = find_heu(q)
            g = q
    print("HS in Func", hs)
    return g

def create(g):
    i = 0
    queue = [copy.deepcopy(initial_state)]
    while not is_goal_state(queue[0]):
        print("Level: ", i)
        g += 1
        num_nodes_at_level = len(queue)
        print("Number of nodes at each level: ", num_nodes_at_level)
        next_node_to_select = find_least_hs(queue)
        queue.clear()
        hs = find_heu(next_node_to_select)
        fs = hs + g
        print("H(s):", hs, "  G(s):", g, "  F(s):", fs)
        print()
        print_graph(next_node_to_select)
        
        current_state = next_node_to_select
        row_index = find_row_index(current_state, 0)
        col_index = find_col_index(current_state, 0)
        
        if up(current_state, row_index, col_index):
            temp = current_state[row_index][col_index]
            current_state[row_index][col_index] = current_state[row_index - 1][col_index]
            current_state[row_index - 1][col_index] = temp
            
            queue.append(copy.deepcopy(current_state))
            temp = current_state[row_index][col_index]
            current_state[row_index][col_index] = current_state[row_index - 1][col_index]
            current_state[row_index - 1][col_index] = temp
        
        if left(current_state, row_index, col_index):
            temp = current_state[row_index][col_index]
            current_state[row_index][col_index] = current_state[row_index][col_index - 1]
            current_state[row_index][col_index - 1] = temp
            
            queue.append(copy.deepcopy(current_state))
            temp = current_state[row_index][col_index]
            current_state[row_index][col_index] = current_state[row_index][col_index - 1]
            current_state[row_index][col_index - 1] = temp
        
        if down(current_state, row_index, col_index):
            temp = current_state[row_index][col_index]
            current_state[row_index][col_index] = current_state[row_index + 1][col_index]
            current_state[row_index + 1][col_index] = temp
            
            queue.append(copy.deepcopy(current_state))
            temp = current_state[row_index][col_index]
            current_state[row_index][col_index] = current_state[row_index + 1][col_index]
            current_state[row_index + 1][col_index] = temp
        
        if right(current_state, row_index, col_index):
            temp = current_state[row_index][col_index]
            current_state[row_index][col_index] = current_state[row_index][col_index + 1]
            current_state[row_index][col_index + 1] = temp
            
            queue.append(copy.deepcopy(current_state))
            temp = current_state[row_index][col_index]
            current_state[row_index][col_index] = current_state[row_index][col_index + 1]
            current_state[row_index][col_index + 1] = temp
        
        i += 1

create(g)
