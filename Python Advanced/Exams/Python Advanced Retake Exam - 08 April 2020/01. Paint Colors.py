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


# Second Way:

# strings = input().split()
#
# main_colors = ["red", "yellow", "blue"]
# secondary_colors = {"orange": ("red", "yellow"), "purple": ("red", "blue"), "green": ("yellow", "blue")}
# made_colors = []
#
# while strings:
#     first_element = strings.pop(0)
#     second_element = ""
#
#     if strings:
#         second_element = strings.pop()
#
#     first_comb = first_element + second_element
#     second_comb = second_element + first_element
#
#     if first_comb in main_colors or first_comb in secondary_colors:
#         made_colors.append(first_comb)
#     elif second_comb in main_colors or second_comb in secondary_colors:
#         made_colors.append(second_comb)
#     else:
#         if len(first_element) > 1:
#             strings.insert(len(strings) // 2, first_element[:-1])
#         if len(second_element) > 1:
#             strings.insert(len(strings) // 2, second_element[:-1])
#
# for i in range(len(made_colors) - 1, -1, -1):
#     current = made_colors[i]
#     if current in secondary_colors and any(x not in made_colors for x in secondary_colors[current]):
#         del made_colors[i]
#
# print(made_colors)