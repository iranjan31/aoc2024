def count_xmas_occurrences(grid, word="XMAS"):
    rows, cols = len(grid), len(grid[0])
    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0), 
        (1, 1), (-1, -1), (1, -1), (-1, 1)
    ]
    
    def search_from(x, y, dx, dy):
        return all(
            0 <= x + k * dx < rows and 0 <= y + k * dy < cols and grid[x + k * dx][y + k * dy] == word[k]
            for k in range(len(word))
        )

    return sum(
        search_from(x, y, dx, dy)
        for x in range(rows)
        for y in range(cols)
        for dx, dy in directions
    )


def count_x_mas_occurrences(grid):
    rows, cols = len(grid), len(grid[0])
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    return sum(
        grid[x][y] == "A" and
        {"M", "S"} == {grid[x - 1][y - 1], grid[x + 1][y + 1]} and
        {"M", "S"} == {grid[x - 1][y + 1], grid[x + 1][y - 1]}
        for x in range(1, rows - 1)
        for y in range(1, cols - 1)
        if is_valid(x - 1, y - 1) and is_valid(x + 1, y + 1) and is_valid(x - 1, y + 1) and is_valid(x + 1, y - 1)
    )


# Read input and process grid
with open('day4_input.txt', 'r') as file:
    grid = [list(row) for row in file.read().splitlines()]

# Count occurrences
print("Total occurrences of XMAS:", count_xmas_occurrences(grid))
print("Total occurrences of X-MAS:", count_x_mas_occurrences(grid))



