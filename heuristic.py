import copy

initial_state = [[8, 3, 4], [1, 7, 2], [5, 6, 0]]  # Initial state
goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Goal state
max_depth = 4  # Maximum depth of the search
queue = []
n = 2
g = 0

def print_state(state):
    for row in state:
        for col in row:
            print(col, end=" ")
        print()
    print()

def can_move_up(state, row_index, col_index):
    if row_index - 1 >= 0:
        return True
    return False

def can_move_down(state, row_index, col_index):
    if row_index + 1 <= n:
        return True
    return False

def can_move_left(state, row_index, col_index):
    if col_index - 1 >= 0:
        return True
    return False

def can_move_right(state, row_index, col_index):
    if col_index + 1 <= n:
        return True
    return False

def find_blank_row_index(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                return i
    return -1

def find_blank_col_index(matrix):
    for row in matrix:
        for j in range(len(row)):
            if row[j] == 0:
                return j
    return -1

def calculate_heuristic(state):
    h = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                h += 1
    return h

def create(g):
    blank_row_index = find_blank_row_index(initial_state)
    blank_col_index = find_blank_col_index(initial_state)
    queue.append(copy.deepcopy(initial_state))
    print_state(queue[0])

    for depth in range(max_depth):
        print("Depth: ", (depth + 1))
        g += 1
        num_nodes_at_depth = len(queue)

        for i in range(num_nodes_at_depth):
            current_state = queue.pop(0)
            blank_row_index = find_blank_row_index(current_state)
            blank_col_index = find_blank_col_index(current_state)

            if can_move_up(current_state, blank_row_index, blank_col_index):
                temp = current_state[blank_row_index][blank_col_index]
                current_state[blank_row_index][blank_col_index] = current_state[blank_row_index - 1][blank_col_index]
                current_state[blank_row_index - 1][blank_col_index] = temp
                h = calculate_heuristic(current_state)
                print("H(s): ", h)
                print("G(s): ", g)
                print("F(s): ", h + g)
                print()
                print_state(current_state)
                queue.append(copy.deepcopy(current_state))
                temp = current_state[blank_row_index][blank_col_index]
                current_state[blank_row_index][blank_col_index] = current_state[blank_row_index - 1][blank_col_index]
                current_state[blank_row_index - 1][blank_col_index] = temp

            

create(g)
