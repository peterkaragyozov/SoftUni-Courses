n = int(input())
longest_intersection = set()

for _ in range(n):
    first_range, second_range = input().split("-")
    first_range_start, first_range_end = first_range.split(",")
    second_range_start, second_range_end = second_range.split(",")
    first_range_start = int(first_range_start)
    first_range_end = int(first_range_end)
    second_range_start = int(second_range_start)
    second_range_end = int(second_range_end)

    first_set = set([x for x in range(first_range_start, first_range_end + 1)])
    second_set = set([x for x in range(second_range_start, second_range_end + 1)])

    intersection = first_set & second_set

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

len_longest_intersection = len(longest_intersection)
str_longest_intersection = [str(x) for x in longest_intersection]
print(f"Longest intersection is [{', '.join(str_longest_intersection)}] with length {len_longest_intersection}")