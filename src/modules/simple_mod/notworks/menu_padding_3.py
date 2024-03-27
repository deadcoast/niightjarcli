import os


def generate_dynamic_interface(menu_title, left_panel_details, right_panel_commands):
    """
    Generate a dynamic CLI interface that adjusts to the window size.

    :param menu_title: str - The title of the menu/interface.
    :param left_panel_details: dict - Details for the left panel content.
    :param right_panel_commands: dict - Commands and descriptions for the right panel.
    :return: str - The dynamic CLI interface template.
    """
    # Get terminal size
    rows, columns = os.get_terminal_size()

    # Calculate widths based on terminal size
    left_panel_width = columns // 2 - 4
    right_panel_width = columns // 2 - 4

    # Constructing the top section
    top_border = "=" * (columns - 2)
    title_row = f"|{menu_title.center(columns - 4)}|"
    separator = "=" * (columns - 2)

    # Constructing the left panel dynamically
    left_panel = ""
    for key, value in left_panel_details.items():
        left_panel += f"| {key.ljust(left_panel_width - 2)}|".ljust(columns // 2)

        # Constructing the right panel with CLI commands dynamically
    right_panel = ""
    for command, description in right_panel_commands.items():
        right_panel += f"| {command.ljust(right_panel_width - 2)}|".ljust(columns // 2)

    # Combine left and right panels
    panels = "\n".join([f"{lp}{rp}" for lp, rp in zip(left_panel.split('\n'), right_panel.split('\n'))])

    # Combine all sections into the final template
    full_system_template = f".{top_border}.\n{title_row}\n.{separator}.\n{panels}\n.{separator}."

    return full_system_template


# Example data for the dynamic template
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

# Generate and display the dynamic interface
dynamic_interface = generate_dynamic_interface(menu_title, left_panel_details, right_panel_commands)
print(dynamic_interface)

