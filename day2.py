import re


def _check_game(game_result: list[str]) -> bool:
    max_counts = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    pulls = game_result.split(";")
    for pull in pulls:
        cubes = pull.split(",")
        for cube in cubes:
            count, color = re.match(r"(\d+)\s+(\w+)", cube.strip()).groups()
            if max_counts.get(color) and max_counts.get(color) < int(count):
                return False
    return True


def possible_game_sum(filename: str) -> int:
    game_sum = 0
    lines = []
    with open(filename, "r") as f:
        lines = f.readlines()
    for line in lines:
        game, result = line.split(":")
        game_num = int(game.split(" ")[1])
        if _check_game(result):
            game_sum += game_num
    return game_sum


def _get_power(result: str) -> int:
    minimums = {
        "green": 0,
        "red": 0,
        "blue": 0
    }
    power = 1
    pulls = result.split(";")
    for pull in pulls:
        cubes = pull.split(',')
        for cube in cubes:
            count, color = re.match(r"(\d+)\s+(\w+)", cube.strip()).groups()
            if int(count) > minimums[color]:
                minimums[color] = int(count)
    for val in minimums.values():
        power *= val
    return power


def get_min_set(filename: str) -> int:
    power_sum = 0
    with open(filename, "r") as f:
        lines = f.readlines()
    for line in lines:
        result = line.split(":")[1]
        power = _get_power(result)
        power_sum += power
    return power_sum


if __name__ == "__main__":
    print(get_min_set("day.data"))
