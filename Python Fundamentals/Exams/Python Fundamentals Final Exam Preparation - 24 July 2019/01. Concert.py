concert_dict = {}
band_play = {}
total_time = 0

while True:
    line = input()
    if line == "start of concert":
        for v in band_play.values():
            total_time += v
        print(f"Total time: {total_time}")

        band_play = dict(sorted(band_play.items(), key=lambda x: (-(x[1]), x[0])))
        for k, v in band_play.items():
            print(f"{k} -> {v}")
        break

    line = line.split("; ")
    cmd = line[0]

    if cmd == "Add":
        band = line[1]
        members = line[2].split(", ")

        if band not in concert_dict:
            concert_dict[band] = []
        for m in members:
            if m not in concert_dict[band]:
                concert_dict[band].append(m)

    elif cmd == "Play":
        band = line[1]
        time = int(line[2])

        if band not in band_play:
            band_play[band] = 0
        band_play[band] += time

final_input = input()
print(final_input)
for member in concert_dict[final_input]:
    print(f"=> {member}")