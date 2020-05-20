from collections import deque


def next_second(hours, minutes, seconds):
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours += 1
        minutes = 0
    if hours == 24:
        hours = 0
    return hours, minutes, seconds


robot_info = input().split(";")
robot_dict = {}
available_robots = deque()
waiting_robots = deque()
products = deque()

time = [int(x) for x in input().split(":")]

product = input()

while product != "End":
    products.append(product)

    product = input()

for robot in robot_info:
    robot_name = robot.split("-")[0]
    robot_time = int(robot.split("-")[1])
    available_robots.append([robot_name, robot_time])
    robot_dict[robot_name] = robot_time

while products:
    for robot in waiting_robots:
        robot_name = robot[0]
        robot[1] -= 1
        if robot[1] <= 0:
            available_robots.append([robot_name, robot_dict[robot_name]])
    waiting_robots = [r for r in waiting_robots if r[1] > 0]

    time = next_second(time[0], time[1], time[2])
    current_product = products.popleft()

    if not available_robots:
        products.append(current_product)
        continue

    current_robot = available_robots.popleft()
    print(f"{current_robot[0]} - {current_product} [{time[0]:02d}:{time[1]:02d}:{time[2]:02d}]")
    waiting_robots.append(current_robot)