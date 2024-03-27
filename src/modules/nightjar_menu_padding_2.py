def generate_full_system_upgrade(menu_title, left_panel_details, right_panel_details, bottom_panel_commands):
    """
    Generate a full-system upgrade for the CLI interface template, focusing on the bottom half with CLI commands.

    :param menu_title: str - The title of the menu/interface.
    :param left_panel_details: dict - Details for the left panel content.
    :param right_panel_details: dict - Details for the right panel content.
    :param bottom_panel_commands: dict - CLI commands and descriptions for the bottom panel.
    :return: str - The upgraded full-system CLI interface template.
    """
    # Constructing the top section
    top_section = f".===================================================================================.\n" \
                  f"||                        - {menu_title.center(54)} -                        ||\n" \
                  f"||=================================================================================||\n"

    # Constructing the left and right panels dynamically
    left_panel = "|| .----------------------------------.  .--------------------------------------.  ||\n"
    for key, value in left_panel_details.items():
        left_panel += f"|| | {key.ljust(32)} |  | {value.ljust(36)} |\n"
    left_panel += "|| '----------------------------------'  '--------------------------------------'  ||\n"

    # Building the bottom panel with CLI commands dynamically
    bottom_panel = "|| .----------------------------------.  .--------------------------------------.  ||\n"
    for command, description in bottom_panel_commands.items():
        bottom_panel += f"|| | {command.ljust(32)} |  | {description.ljust(36)} |\n"
    bottom_panel += "|| '----------------------------------'  '--------------------------------------'  ||\n"
    bottom_panel += "||=================================================================================||\n"

    # CLI quick commands
    quick_commands = "|| [>] " + " - ".join(bottom_panel_commands.keys()) + " |  | --get --all --lay <--, --> ...          ||\n"
    bottom_border = "'==================================================================================='"

    # Combine all sections into the final template
    full_system_template = top_section + left_panel + bottom_panel + quick_commands + bottom_border

    return full_system_template

# Example data for the upgraded full-system template
menu_title = "CHRONO NAVIGATIONAL INTERFACE"
left_panel_details = {
    "nightjar flight HISTORY": "_time_22:15",
    "[egg_files]": "--help",
}
right_panel_details = {
    "CURRENT MENU": "Main Menu",
    "purpose": "Short concise purpose"
}
bottom_panel_commands = {
    "help": "Display commands",
    "intro": "Introduction to nightjar",
    "map": "Display the nightjar map",
    "nest": "List system Commands",
    "basket": "List file Categories"
}

# Generate and display the full-system upgraded interface
print(generate_full_system_upgrade(menu_title, left_panel_details, right_panel_details, bottom_panel_commands))

