def create_framed_digital_clock(time_str):
    # Representation of each digit on a 7-segment display (0-9), adjusted for tubes
    digits = [
        " _     _  _     _  _  _  _  _ ",
        "| |  | _| _||_||_ |_   ||_||_|",
        "|_|  ||_  _|  | _||_|  ||_| _|",
        "                               "
    ]

    # Additional layer for bottom part of the frame
    bottom_frame = "'-----'  '-----'     '-----' '-----'  '-----' '-----'"

    # Mapping the time string (hh:mm:ss) to the digits representation
    digit_map = {str(num): index for index, num in enumerate("0123456789")}
    lines = ["", "", "", ""]

    for char in time_str:
        if char in digit_map:
            index = digit_map[char] * 3
            for row in range(4):
                if row < 3:
                    lines[row] += digits[row][index:index + 3]
                else:
                    lines[row] += " .-----. "
        else:
            # For non-digit characters (colon), add spacing and framing as appropriate
            for row in range(4):
                if row < 3:
                    lines[row] += "  "
                else:
                    lines[row] += "     "  # Spacing for between digits

    # Adding the bottom frame to the last line
    lines.append(bottom_frame)

    return "\n".join(lines)


# Example time (12:34:56)
time_str = "12:34:56"
clock_display = create_framed_digital_clock(time_str)
print(clock_display)
