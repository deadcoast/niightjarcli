from itertools import zip_longest
import shutil
import math
import os

import colorama

# Define color constants
COLOR_TITLE = colorama.Fore.MAGENTA  # Bright magenta
COLOR_KEY = colorama.Fore.BLUE  # Bright blue
COLOR_VALUE = colorama.Fore.GREEN  # Bright green
COLOR_RESET = colorama.Style.RESET_ALL  # Reset to default terminal color

# Initialize colorama module only once when the script is run
colorama.init()


def generate_dynamic_colored_interface(menu_title: str, left_panel_details: dict, right_panel_commands: dict) -> str:
    """
    Generate a dynamic colored CLI interface that adjusts to the current terminal width.

    :param menu_title: str - The title of the menu/interface.
    :param left_panel_details: dict - Details for the left panel content.
    :param right_panel_commands: dict - Commands and descriptions for the right panel.
    :return: str - The dynamic colored CLI interface template.
    """
    # Get the current terminal size dynamically
    terminal_size = os.get_terminal_size()
    columns = terminal_size.columns

    # Calculate widths based on terminal size
    left_panel_width = columns // 2
    right_panel_width = columns // 2

    # Constructing the top section with color
    top_border = "=" * columns
    title_row = f"{COLOR_TITLE}{menu_title.center(columns)}{COLOR_RESET}"
    separator = "=" * columns

    # Handle the case where left_panel_details and right_panel_commands have different lengths
    max_length = max(len(left_panel_details), len(right_panel_commands))
    left_panel_details = dict(zip_longest(left_panel_details.keys(), left_panel_details.values(), fillvalue=('', '')))
    right_panel_commands = dict(zip_longest(right_panel_commands.keys(), right_panel_commands.values(), fillvalue=('', '')))

    # Constructing the left and right panels together using list comprehension
    panels = [f"{COLOR_KEY}{key:<{left_panel_width - 2}}{COLOR_VALUE}{command:<{right_panel_width - 2}}"
              for (key, value), (command, description) in zip(left_panel_details.items(), right_panel_commands.items())]
    panels = '\n'.join(panels)

    # Combine all sections into the final template with color
    full_system_template = [top_border,
                            COLOR_RESET + title_row,
                            separator,
                            panels,
                            separator]
    full_system_template = '\n'.join(full_system_template)

    return full_system_template


# Example data for the dynamic colored template
menu_title = "CHRONO NAVIGATIONAL INTERFACE"
left_panel_details = {
    "nightjar flight HISTORY": "_time_22:15",
    "[egg_files]": "--help"
}
right_panel_commands = {
    "help": "Display commands",
    "intro": "Introduction to nightjar",
    "map": "Display the nightjar map",
    "nest": "List system Commands",
    "basket": "List file Categories"
}

# Generate and display the dynamic colored interface
# Note: The colors will only display correctly in a terminal that supports ANSI color codes.
dynamic_colored_interface = generate_dynamic_colored_interface(menu_title, left_panel_details, right_panel_commands)
print(dynamic_colored_interface)
