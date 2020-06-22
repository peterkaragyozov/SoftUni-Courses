line_string = input().split()
main_colours = ["red", "yellow", "blue"]
secondary_colours = {"orange": ["red", "yellow"], "purple": ["blue", "red"], "green": ["yellow", "blue"]}
collected_colours = []

while line_string:
    first_element = line_string.pop()
    last_element = "" if not line_string else line_string.pop(0)

    if first_element + last_element in main_colours:
        collected_colours.append(first_element + last_element)
        main_colours.remove(first_element + last_element)
    elif last_element + first_element in main_colours:
        collected_colours.append(last_element + first_element)
        main_colours.remove(last_element + first_element)

    elif first_element + last_element in secondary_colours:
        collected_colours.append(first_element + last_element)
    elif last_element + first_element in secondary_colours:
        collected_colours.append(last_element + first_element)

    else:
        first_element = first_element[:-1]
        last_element = last_element[:-1]

        if first_element:
            line_string.insert(len(line_string) // 2, first_element)
        if last_element:
            line_string.insert(len(line_string) // 2, last_element)

for colour in collected_colours:
    if secondary_colours.get(colour):
        if any(x not in collected_colours for x in secondary_colours[colour]):
            collected_colours.remove(colour)
            del secondary_colours[colour]

print(collected_colours)