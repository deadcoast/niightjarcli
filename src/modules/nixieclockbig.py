# First, let's define a function to create the digits 0-9 in ASCII art
def create_digits():
    # Representation of each digit on a 7-segment display (0-9)
    digit_segments = {
        '0': [" _ ", "| |", "|_|"],
        '1': ["   ", "  |", "  |"],
        '2': [" _ ", " _|", "|_ "],
        '3': [" _ ", " _|", " _|"],
        '4': ["   ", "|_|", "  |"],
        '5': [" _ ", "|_ ", " _|"],
        '6': [" _ ", "|_ ", "|_|"],
        '7': [" _ ", "  |", "  |"],
        '8': [" _ ", "|_|", "|_|"],
        '9': [" _ ", "|_|", " _|"]
    }
    return digit_segments

# Next, a function to put a digit within a tube
def put_digit_in_tube(digit):
    digit_segments = create_digits()
    digit_lines = digit_segments[digit]
    framed_digit = [
        ".-----.",
        f"|{digit_lines[0]}|",
        f"|{digit_lines[1]}|",
        f"|{digit_lines[2]}|",
        "'-----'"
    ]
    return "\n".join(framed_digit)

# Function to create a clock display with digits in tubes
def create_clock_with_tubes(time_str):
    # Split the time string into its constituent parts
    digits = list(time_str.replace(':', ''))  # Remove colon for simplicity

    # Put each digit in its tube
    tube_digits = [put_digit_in_tube(digit) for digit in digits]

    # Join the tubes horizontally
    clock_display = "\n".join(["  ".join(lines) for lines in zip(*[tube.split('\n') for tube in tube_digits])])

    return clock_display

# Example: create and print the clock display for "12:34:56"
time_str = "12:34:56"
clock_display = create_clock_with_tubes(time_str)
print(clock_display)
