side_size = float(input())
sheets_number = int(input())
paper_sheet_area = float(input())

gift_box_area = side_size * side_size * 6

covered_area = 0
for sheet in range(1, sheets_number + 1):
    if sheet % 3 == 0:
        covered_area += 25 / 100 * paper_sheet_area
    else:
        covered_area += paper_sheet_area

percentage_covered = covered_area / gift_box_area * 100
print(f"You can cover {percentage_covered:.2f}% of the box.")