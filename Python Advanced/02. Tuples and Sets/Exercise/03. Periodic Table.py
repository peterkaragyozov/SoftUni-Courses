n = int(input())
all_elements = set()

for _ in range(n):
    elements = set(input().split(" "))
    all_elements = all_elements | elements
    # 2) all_elements |= elements
    # 3) all_elements.union(elements)

# for element in all_elements:
#     print(element)
print("\n".join(all_elements))