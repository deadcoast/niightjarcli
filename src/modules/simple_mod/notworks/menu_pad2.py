def generate_nightjar_history_template(time, menu_histories):
    """
    Generate a detailed ASCII section for the Nightjar Flight History, upgraded to remove comments and
    ensure dynamic adjustment to terminal width while adding color for emphasis.

    :param time: str - Current system time.
    :param menu_histories: list - List containing strings representing the last three menus visited.
    :return: str - The Nightjar Flight History ASCII section with dynamic width and color.
    """
    try:
        columns = os.get_terminal_size().columns
    except OSError:
        columns = 80  # Default to 80 columns if terminal size cannot be determined

    # Calculate dynamic sizing
    left_panel_width = columns // 2
    right_panel_width = columns - left_panel_width - 2  # Account for border

    # ANSI Color Codes
    color_time = "\033[93m"  # Yellow for time
    color_menu = "\033[96m"  # Cyan for menu history
    color_reset = "\033[0m"  # Reset to default

    # Building the template with dynamic width and colored text
    top_border = f"{'=' * (columns - 2)}"
    title = "nightjar flight HISTORY".center(columns - 2)
    time_str = f"{color_time}_time_{time}{color_reset}".ljust(left_panel_width)
    flight_plan_title = "Flight Plan, History of the User Menu Navigation".ljust(right_panel_width)

    # Menu Histories
    history_lines = "\n".join([
        f"{color_menu}1{menu_histories[0]} 2{menu_histories[1]} 3{menu_histories[2]}{color_reset}".ljust(left_panel_width) +
        " ".ljust(right_panel_width) for _ in range(3)  # Simulating multiple lines for demonstration
    ])

    bottom_border = f"{'=' * (columns - 2)}"

    # Combine all parts
    history_template = f".{top_border}.\n|{title}|\n|{time_str}|{flight_plan_title}|\n{history_lines}\n'{bottom_border}'"

    return history_template

# Example usage with specific time and the last three menus visited
time = "22:15"
menu_histories = ["Main Menu", "Settings", "Help"]

# Generate and display the Nightjar Flight History section with dynamic adjustment and color
print(generate_nightjar_history_template(time, menu_histories))

