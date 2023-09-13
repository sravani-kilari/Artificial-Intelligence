def create(initial_state, level):
    def is_valid_move(x, y):
        return 0 <= x < 3 and 0 <= y < 3

    def apply_move(state, move):
        new_state = [row[:] for row in state]  # Create a copy of the current state
        x, y = get_blank_position(new_state)
        if move == 'Up' and is_valid_move(x - 1, y):
            new_state[x][y], new_state[x - 1][y] = new_state[x - 1][y], new_state[x][y]
        elif move == 'Down' and is_valid_move(x + 1, y):
            new_state[x][y], new_state[x + 1][y] = new_state[x + 1][y], new_state[x][y]
        elif move == 'Left' and is_valid_move(x, y - 1):
            new_state[x][y], new_state[x][y - 1] = new_state[x][y - 1], new_state[x][y]
        elif move == 'Right' and is_valid_move(x, y + 1):
            new_state[x][y], new_state[x][y + 1] = new_state[x][y + 1], new_state[x][y]
        return new_state

    def get_blank_position(state):
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    return i, j

    def generate_states(current_state, current_level):
        if current_level == 0:
            return [current_state]

        next_states = []
        for move in ['Up', 'Down', 'Left', 'Right']:
            new_state = apply_move(current_state, move)
            next_states += generate_states(new_state, current_level - 1)

        return next_states

    if level < 0:
        print("Level number should be non-negative.")
        return

    generated_states = generate_states(initial_state, level)
    for idx, state in enumerate(generated_states):
        print(f"State {idx + 1}:")
        for row in state:
            print(row)
        print()

# Example usage:
initial_state = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]
level = 2
create(initial_state, level)
