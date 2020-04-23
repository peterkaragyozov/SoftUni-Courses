capacity = int(input())

dictionary = {}

while True:
    line = input()
    if line == "Statistics":
        print(f"Users count: {len(dictionary)}")
        sorted_dictionary = dict(sorted(dictionary.items(), key=lambda x: (-x[1][1], x[0])))

        for k,v in sorted_dictionary.items():
            print(f"{k} - {sum(v)}")
        break

    line = line.split("=")
    cmd = line[0]
    if cmd == "Add":
        username = line[1]
        sent = int(line[2])
        received = int(line[3])
        if username not in dictionary:
            dictionary[username] = [0] * 2
            dictionary[username][0] = sent
            dictionary[username][1] = received
    elif cmd == "Message":
        sender = line[1]
        receiver = line[2]
        if (sender in dictionary) and (receiver in dictionary):
            dictionary[sender][0] += 1
            if dictionary[sender][0] + dictionary[sender][1] == capacity:
                print(f"{sender} reached the capacity!")
                del dictionary[sender]
            dictionary[receiver][1] += 1
            if dictionary[receiver][1] + dictionary[receiver][0] == capacity:
                print(f"{receiver} reached the capacity!")
                del dictionary[receiver]
    elif cmd == "Empty":
        username = line[1]
        # в случая трия целия речник и съответния юзър. Ако грешно съм разбрал,
        # тогава пробвам да запазя речника и юзърите, но с 0 за стойности при send/received
        if username == "All":
            dictionary = {}
        else:
            del dictionary[username]