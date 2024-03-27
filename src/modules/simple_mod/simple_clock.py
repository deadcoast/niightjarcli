def create_digital_clock(time_str):
    # Representation of each digit on a 7-segment display (0-9)
    digits = [
        " _     _  _     _  _  _  _  _ ",
        "| |  | _| _||_||_ |_   ||_||_|",
        "|_|  ||_  _|  | _||_|  ||_| _|",
    ]

    # Mapping the time string (hh:mm:ss) to the digits representation
    digit_map = {str(num): index for index, num in enumerate("0123456789")}
    lines = ["", "", ""]

    for char in time_str:
        if char in digit_map:
            index = digit_map[char] * 3
            for row in range(3):
                lines[row] += digits[row][index:index + 3]
        else:
            # For non-digit characters, add a space or appropriate separator
            for row in range(3):
                lines[row] += "   " if char == ":" else char

    return "\n".join(lines)


# Example time (12:34:56)
time_str = "12:34:56"
clock_display = create_digital_clock(time_str)
print(clock_display)
