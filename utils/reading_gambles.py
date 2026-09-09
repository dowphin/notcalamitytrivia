def read_slots(grid: list[list[str]]) -> list[list[str]]:  # read the grid, probably gonna more methods for each combination

    found_combos = []
    found_combos.append(rows(grid))
    found_combos.append(columns(grid))
    found_combos.append(diagonals(grid))
    found_combos.append(v(grid))
    found_combos.append(triangle(grid))
    found_combos.append(eye(grid))
    found_combos.append(jackpot(grid))

    return found_combos


def rows(grid: list[list[str]]) -> list[str]:  # looks for any runs in a row

    # brute force method of checking if a row contains a run of 3 or more of the same item

    found_runs = []

    for i in range(3):

        count = 1
        item = ""
        # iterates through entire grid, checks if 3 in a row
        for j in grid[i]:
            if j == item:
                count += 1
            else:
                if count >= 3:
                    found_runs.append(f"Found {count} {item}s in row {i + 1}")
                item = j
                count = 1
        # final check necessary in case last 3 is a run
        if count >= 3:
            found_runs.append(f"Found {count} {item}s in row {i + 1}")

    return found_runs


def columns(grid: list[list[str]]) -> list[str]:  # looks for any runs in a column

    # similar approach, another brute force method of checking is a column contains a run of 3

    found_runs = []

    for i in range(5):

        # iterates yada yada you know the drill
        for j in range(3):

            if j == 0:

                item = grid[j][i]
                count = 1

            else:

                if grid[j][i] == item:
                    count += 1

                else:
                    item = grid[j][i]
                    count = 1

        if count >= 3:
            found_runs.append(f"Found {count} {item}s in column {i + 1}")

    return found_runs


def diagonals(grid: list[list[str]]) -> list[str]:  # checks every diagonal

    found_runs = []

    for i in range(3):  # all diagonals left to right

        diagonal = set([grid[0][i], grid[1][i + 1], grid[2][i + 2]])  # gonna use set magic cuz i can't be bothered to write readable code atp

        if len(diagonal) == 1:
            found_runs.append(
                f"Found diagonal of {grid[0][i]}s going left to right, top to bottom from columns {i + 1} - {i + 3}")

    for i in range(3):  # all diagonals right to left

        diagonal = set([grid[2][i], grid[1][i + 1], grid[0][i + 2]])  # gonna use set magic cuz i can't be bothered to write readable code atp

        if len(diagonal) == 1:
            found_runs.append(
                f"Found diagonal of {grid[2][i]}s going left to right, bottom to top from columns {i + 1} - {i + 3}")

    return found_runs


def v(grid: list[list[str]]) -> list[str]:  # v shape, essentially simultaneous outer diagonals

    found_runs = []

    # v-shaped pattern

    v_pattern = set()

    aux_string = "21012"

    for i in range(5):
        v_pattern.add(grid[int(aux_string[i])][i])  # more set magic, should hopefully be the v shape

    if len(v_pattern) == 1:
        found_runs.append(f"Found ^-shape of {grid[2][0]}s")

    v_pattern.clear()

    aux_string = "01210"

    for i in range(5):
        v_pattern.add(grid[int(aux_string[i])][i])  # more set magic, should hopefully be the ^ shape

    if len(v_pattern) == 1:
        found_runs.append(f"Found V-shape of {grid[0][0]}s")

    return found_runs


def triangle(grid: list[list[str]]) -> list[str]:  # triangle, v shapes along with corresponding 5 in a row

    found_runs = []

    aux_string = "21012"

    std_triangle = set()

    for i in range(5):
        std_triangle.add(grid[int(aux_string[i])][i])
        std_triangle.add(grid[2][i])

    if len(std_triangle) == 1:
        found_runs.append(f"Found triangle shape of {grid[2][0]}s")

    aux_string = "01210"

    inv_triangle = set()

    for i in range(5):
        inv_triangle.add(grid[int(aux_string[i])][i])
        inv_triangle.add(grid[0][i])

    if len(inv_triangle) == 1:
        found_runs.append(f"Found inverted triangle shape of {grid[0][0]}s")

    return found_runs


def eye(grid: list[list[str]]) -> list[str]:  # eye shape, idk how to explain this one

    found_runs = []

    indexes = ["123", "0134", "123"]

    eye_pattern = set()

    for i in range(len(indexes)):
        for j in range(len(indexes[i])):
            eye_pattern.add(grid[i][int(indexes[i][j])])

    if len(eye_pattern) == 1:
        found_runs.append(f"Found eye shape of {grid[0][1]}s")

    return found_runs

def jackpot(grid: list[list[str]]) -> list[str]:  # jackpot !!!

    found_runs = []

    jackpot_pattern = set()

    for i in range(3):
        for j in range(5):
            jackpot_pattern.add(grid[i][j])

    if len(jackpot_pattern) == 1:
        found_runs.append(f"Found jackpot of {grid[0][1]}s")

    return found_runs

#DEBUG CODE

#test_grid = [["]", "n", "A", "h", "b"], ["]", "A", "b", "A", "z"], ["A", "A", "A", "A", "A"]]

#test_grid = [["A", "A", "A", "A", "A"], ["]", "A", "b", "A", "z"], ["a", "X", "A", "bn", "z"]]

#test_grid = [["x", "A", "A", "A", "a"], ["A", "A", "x", "A", "A"], ["a", "A", "A", "A", "z"]]

#test_grid = [["A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A"]]

#for i in test_grid:
#    print(" ".join(i))

#combs = read_slots(test_grid)

#for i in combs:
#    print("\n".join(i))