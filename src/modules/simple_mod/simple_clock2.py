def create_framed_digital_clock_v3(time_str):
    # Define the digit representations for a 7-segment display
    digits = {
        '0': ['._.', '|.|', '|_|'],
        '1': ['...', '..|', '..|'],
        '2': ['._.', '._|', '|_.'],
        '3': ['._.', '._|', '._|'],
        '4': ['...', '|_|', '..|'],
        '5': ['._.', '|_.', '._|'],
        '6': ['._.', '|_.', '|_|'],
        '7': ['._.', '..|', '..|'],
        '8': ['._.', '|_|', '|_|'],
        '9': ['._.', '|_|', '..|'],
        ':': [' ', 'o', 'o', ' ']
    }

    # Initialize the frame for the entire clock
    clock_frame = [""] * 5  # 5 lines high

    for char in time_str:
        for line in range(3):
            if char == ":":
                clock_frame[line + 1] += " " + digits[char][line] + " "  # Center the colon vertically
            else:
                clock_frame[line + 1] += digits[char][line] + "  "
        clock_frame[0] += ".-----.  "  # Top frame
        clock_frame[4] += "'-----'  "  # Bottom frame

    return "\n".join(clock_frame)


# Example time string
time_str = "12:34:56"
clock_display_v3 = create_framed_digital_clock_v3(time_str)
print(clock_display_v3)

