n_length, m_length = [int(x) for x in input().split(" ")]

n = set()
m = set()

for _ in range(n_length):
    number = int(input())
    n.add(number)

for _ in range(m_length):
    number = int(input())
    m.add(number)

intersection = n.intersection(m)
for number in intersection:
    print(number)