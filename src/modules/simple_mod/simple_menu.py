def aesthetic_cli_menu():
    # Define menu items
    menu_items = [
        "1. View Current Time",
        "2. Set Alarm",
        "3. Timer",
        "4. World Clock",
        "5. Exit"
    ]

    # Build the CLI menu with an aesthetic ASCII art style
    menu_art = """
  .----------------------------------------------------------------.
  |                       ~ AESTHETIC CLI MENU ~                   |
  |----------------------------------------------------------------|
  """

    for item in menu_items:
        menu_art += f"|  {item.ljust(58)}|\n"

    menu_art += "  '----------------------------------------------------------------'\n"

    return menu_art


# Display the aesthetic CLI menu
print(aesthetic_cli_menu())
