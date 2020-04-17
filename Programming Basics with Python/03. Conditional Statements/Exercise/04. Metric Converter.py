number_input = float(input())
measurement_input = input()
measurement_output = input()

if measurement_input == measurement_output:
    print(number_input)

else:
    if measurement_input == "mm":
        value_cm = number_input / 10
        value_m = number_input / 1000
        if measurement_output == "cm":
            print(f"{value_cm:.3f}")
        elif measurement_output == "m":
            print(f"{value_m:.3f}")

    elif measurement_input == "cm":
        value_mm = number_input * 10
        value_m = number_input / 100
        if measurement_output == "mm":
            print(f"{value_mm:.3f}")
        elif measurement_output == "m":
            print(f"{value_m:.3f}")

    elif measurement_input == "m":
        value_cm = number_input * 100
        value_mm = number_input * 1000
        if measurement_output == "cm":
            print(f"{value_cm:.3f}")
        if measurement_output == "mm":
            print(f"{value_mm:.3f}")