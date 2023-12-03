import regex as re


def sum_call_values(filename: str) -> int:
    with open(filename, "r") as f:
        lines = f.readlines()
        cal_sum = 0
        for line in lines:
            num_vales = re.findall("\d", line)
            num_to_add = int(f"{num_vales[0]}{num_vales[-1]}")
            cal_sum += num_to_add
        return cal_sum

def _get_number(raw_num: str) -> str:
    string_to_num_map = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    if raw_num.isdigit():
        return raw_num
    else:
        return string_to_num_map[raw_num]


def sum_call_values_strings(filename: str) -> int:
    regex = "(one|two|three|four|five|six|seven|eight|nine|\d)"
    
    with open(filename, "r") as f:
        lines = f.readlines()
        cal_sum = 0
        for line in lines:
            num_values = re.findall(regex, line, overlapped=True)
            num_to_add = int(f"{_get_number(num_values[0])}{_get_number(num_values[-1])}")
            print(f"{num_values} -> {num_to_add}")
            cal_sum += num_to_add
        return cal_sum


if __name__ == "__main__":
    # print(sum_call_values("day1.data"))
    print(sum_call_values_strings("day1.data"))
