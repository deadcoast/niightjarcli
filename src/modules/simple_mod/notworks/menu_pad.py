def generate_nightjar_history_template_enhanced(time, menu_histories):
    """
    Generate a detailed ASCII section for the Nightjar Flight History, preserving all ASCII art and adding dynamic content.

    :param time: str - Current system time.
    :param menu_histories: tuple - A tuple containing three strings representing the last three menus visited.
    :return: str - The Nightjar Flight History ASCII section.
    """
    # ASCII art preserved and dynamic content added
    history_template = f"""
.===================================================================================.
||                        - nightjar flight HISTORY -                              ||
||=================================================================================||
|| .----------------------------------.  .--------------------------------------.  ||
|| |                  _time_{time:<43}|  |         Flight Plan, History         |  ||
|| |   .--------------------------.   |  |    of the User Menu Navigation       |  ||
|| |   |   1{menu_histories[0]:<10}2{menu_histories[1]:<10}3{menu_histories[2]:<10}||
|| |   |  \\   / \\   / \\   / \\  / \\   / \\  / \\  / \\   / \\  / \\  / \\   /  ||
|| |   |   \\ /   \\ /   \\ /   \\/   \\ /   \\/   \\/   \\ /   \\/   \\/   \\ /|  ||
|| |   '--------------------------'   |  |                                      |  ||
|| '----------------------------------'  '--------------------------------------'  ||
'==================================================================================='
"""

    return history_template

# Example usage with specific time and the last three menus visited
time = "22:15"
menu_histories = ("Main Menu", "Settings", "Help")

# Generate and display the Nightjar Flight History section with all ASCII art preserved
print(generate_nightjar_history_template_enhanced(time, menu_histories))
