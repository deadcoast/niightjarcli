import os


def colorize(text, color_code):
    """Apply ANSI color code to the text."""
    return f"\033[{color_code}m{text}\033[0m"


def generate_interface():
    """
    Generate a structured CLI interface with color enhancements.
    """
    try:
        columns = os.get_terminal_size().columns
    except OSError:
        columns = 80  # Default width if terminal size cannot be determined

    # Color Codes
    header_color = "95"  # Light Magenta
    key_color = "94"  # Light Blue
    value_color = "92"  # Light Green
    reset_color = "0"  # Reset to default

    # Building the interface
    top_border = "=" * columns
    title = "CHRONO NAVIGATIONAL INTERFACE".center(columns)
    separator = "=" * columns

    # Left and right panel content, hardcoded for demonstration
    left_panel_content = [
        colorize("nightjar flight HISTORY", key_color),
        colorize("egg_files --help", key_color)
    ]
    right_panel_content = [
        colorize("_time_22:15", value_color),
        colorize("Script Cheatsheet: Basic Commands", value_color),
        colorize("help - Display commands", value_color),
        colorize("intro - Introduction to Nightjar", value_color),
        colorize("map - Display the Nightjar map", value_color),
        colorize("nest - List system commands", value_color),
        colorize("basket - List file categories", value_color)
    ]

    # Merging panels with padding
    merged_content = "\n".join([
        f"| {left.ljust(columns // 2 - 2)}|{right.ljust(columns // 2)}"
        for left, right in zip(left_panel_content, right_panel_content)
    ])

    # Assembling the interface
    interface = f"{colorize(top_border, header_color)}\n" \
                f"{colorize(title, header_color)}\n" \
                f"{colorize(separator, header_color)}\n" \
                f"{merged_content}\n" \
                f"{colorize(separator, header_color)}"

    return interface


# Generate and print the interface
print(generate_interface())
