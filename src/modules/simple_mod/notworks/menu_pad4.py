import os

def colorize(text, color_code):
    return f"\033[{color_code}m{text}\033[0m"

def generate_full_dynamic_colored_interface(menu_title, left_panel_details, right_panel_commands):
    """
    Generate a full-system, dynamic, and colored CLI interface template.
    Adjusts to the window size and includes detailed ASCII art and functionalities.
    """
    try:
        columns = os.get_terminal_size().columns
    except OSError:
        columns = 80  # Default to 80 columns if terminal size cannot be determined

    # ANSI Color Codes for styling
    title_color = "1;35"  # Bright Magenta
    section_title_color = "1;34"  # Bright Blue
    content_color = "0;37"  # White
    command_color = "1;32"  # Bright Green

    # Header and Footer
    top_border = colorize("=" * columns, content_color)
    title_row = colorize(f"{menu_title.center(columns)}", title_color)
    separator = colorize("=" * (columns - 2), content_color)

    # Left Panel
    left_panel = ""
    for title, content in left_panel_details.items():
        left_panel += colorize(f"| {title.ljust(columns // 2 - 4)}", section_title_color)
        left_panel += colorize(f"| {content.ljust(columns // 2 - 4)}\n", content_color)

    # Right Panel Commands
    right_panel = ""
    for command, description in right_panel_commands.items():
        cmd_text = f"{command} - {description}"
        right_panel += colorize(f"| {cmd_text.ljust(columns // 2 - 4)}\n", command_color)

    # Combine Panels
    panels = ""
    left_lines = left_panel.strip().split('\n')
    right_lines = right_panel.strip().split('\n')
    max_lines = max(len(left_lines), len(right_lines))
    for i in range(max_lines):
        left_line = left_lines[i] if i < len(left_lines) else " " * (columns // 2 - 2)
        right_line = right_lines[i] if i < len(right_lines) else " " * (columns // 2 - 2)
        panels += f"{left_line}{right_line}\n"

    # Final Assembly
    interface = f"{top_border}\n{title_row}\n{separator}\n{panels}{separator}"

    return interface

# Example Inputs
menu_title = "CHRONO NAVIGATIONAL INTERFACE"
left_panel_details = {
    "nightjar flight HISTORY": "_time_22:15",
    "egg_files --help": "Script Cheatsheet: Basic Commands",
}
right_panel_commands = {
    "help": "Display commands",
    "intro": "Introduction to Nightjar",
    "map": "Display the Nightjar map",
    "nest": "List system commands",
    "basket": "List file categories",
}

# Generate the interface
interface = generate_full_dynamic_colored_interface(menu_title, left_panel_details, right_panel_commands)
print(interface)
