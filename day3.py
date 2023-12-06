from typing import List, Tuple, Set

symbols_list = [
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "_",
    "+",
    "-",
    "=",
    "{",
    "}",
    "[",
    "]",
    "|",
    ";",
    ":",
    ",",
    "<",
    ">",
    "?",
    "/",
    "`",
    "~",
]


def get_symbol_locations(
    matrix: List[str], valid_symbol=symbols_list
) -> List[Tuple[int, int]]:
    symbol_coords = []
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell in valid_symbol:
                symbol_coords.append((i, j))
    return symbol_coords


def find_start_coord(
    matrix: List[str], coordinates: Tuple[int, int]
) -> Tuple[int, int]:
    row, col = coordinates
    valid = True
    while valid:
        try:
            prev_col = col - 1
            prev_cell = matrix[row][prev_col]
        except IndexError:
            return (row, col)
        if prev_cell.isnumeric():
            col = prev_col
        else:
            return (row, col)


def has_number_neighbor(
    matrix: List[str], coordinates: Tuple[int, int], min_length: int = 1
) -> List[Tuple] | None:
    row, col = coordinates
    num_neighbors = []
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            try:
                cell = matrix[i][j]
            except IndexError:
                continue
            if cell.isnumeric():
                num_neighbors.append(find_start_coord(matrix, (i, j)))
    if num_neighbors:
        neighbor_set = set(num_neighbors)
        if len(neighbor_set) >= min_length:
            return neighbor_set
    return None


def get_full_number(matrix: List[str], coordinate: Tuple[int, int]) -> int:
    row, col = coordinate
    digits = [matrix[row][col]]
    while True:
        next_col = col + 1
        try:
            next_cell = matrix[row][next_col]
        except IndexError:
            return int("".join(digits))
        if next_cell.isnumeric():
            col = next_col
            digits.append(next_cell)
        else:
            return int("".join(digits))


def get_sum(matrix: List[str], number_coords: Set[Tuple[int, int]]) -> int:
    engine_sum = 0
    for coordinate in number_coords:
        num = get_full_number(matrix, coordinate)
        engine_sum += num
    return engine_sum


def get_engine_sum():
    with open("day.data", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    symbol_coords = get_symbol_locations(lines)
    num_coords = set()
    for coord in symbol_coords:
        result = has_number_neighbor(lines, coord)
        if result:
            num_coords.update(result)
    return get_sum(lines, num_coords)


def calc_gear_ratio(matrix: List[str], num_coords: Set[Tuple[int, int]]) -> int:
    gear_ratio = 1
    for coordinate in num_coords:
        num = get_full_number(matrix, coordinate)
        gear_ratio *= num
    return gear_ratio


def get_sum_gear_ratios(matrix: List[str], num_coords: List[Set[Tuple[int, int]]]) -> int:
    sum_gear_ratios = 0
    for gear_coordinates in num_coords:
        gear_ratio = calc_gear_ratio(matrix, gear_coordinates)
        sum_gear_ratios += gear_ratio
    return sum_gear_ratios


def get_gear_ratio():
    with open("day.data", "r") as f:
        lines = [line.strip() for line in f.readlines()]

    symbol_coords = get_symbol_locations(lines, ["*"])
    num_coords = []
    for coord in symbol_coords:
        result = has_number_neighbor(lines, coord, 2)
        if result:
            num_coords.append(result)
    return get_sum_gear_ratios(lines, num_coords)


if __name__ == "__main__":
    print(get_engine_sum())
    print(get_gear_ratio())
