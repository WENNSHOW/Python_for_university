'''
import re


def main(input_string):
    pattern = r"`(\w+)\s*=\s*#(-?\d+);"

    matches = re.findall(pattern, input_string)

    parsed_result = [(key, int(value)) for key, value in matches]

    return parsed_result


print(main("do( opt `maveor = #895; ) ( opt `sous =#8099;)( opt `leon_215 = #7640;) done"))
print(main("do (opt `diedat = #5990; ) (opt `learre=#-4966; ) done"))
'''


def main(input_string):
    parsed_result = []
    start = input_string.find("`") + 1
    while start != -1:
        end = input_string.find("=", start)
        key = input_string[start:end].strip().replace("`", "")
        start = end + 1
        end = input_string.find(";", start)
        value = int(input_string[start:end].strip().lstrip("#"))
        parsed_result.append((key, value))
        start = input_string.find("(", end)
        if start != -1:
            start += 1
            start = input_string.find("`", start)
    return parsed_result


print(main("do( opt `maveor = #895; ) ( opt `sous =#8099;)( opt `leon_215 = #7640;) done"))
print(main("do (opt `diedat = #5990; ) (opt `learre=#-4966; ) done"))

