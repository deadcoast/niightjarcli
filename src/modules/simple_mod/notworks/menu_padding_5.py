import os

def colorize(text, color_code):
    """
    Apply ANSI color codes to the given text.

    Args:
        text (str): The text to be colorized.
        color_code (str): The ANSI color code to be applied.

    Returns:
        str: The colorized text.
    """
    if not isinstance(text, str):
        raise ValueError("The 'text' input must be a string.")
    try:
        return f"\033[{color_code}m{text}\033[0m"
    except Exception as e:
        print(f"Error occurred while formatting string: {e}")
        return text

    if not isinstance(text, str) or not isinstance(color_code, str):
        return "Invalid input parameters"

    valid_color_codes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70", "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88", "89", "90", "91", "92", "93", "94", "95", "96", "97", "98", "99", "100", "101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "111", "112", "113", "114", "115", "116", "117", "118", "119", "120", "121", "122", "123", "124", "125", "126", "127", "128", "129", "130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "140", "141", "142", "143", "144", "145", "146", "147", "148", "149", "150", "151", "152", "153", "154", "155", "156", "157", "158", "159", "160", "161", "162", "163", "164", "165", "166", "167", "168", "169", "170", "171", "172", "173", "174", "175", "176", "177", "178", "179", "180", "181", "182", "183", "184", "185", "186", "187", "188", "189", "190", "191", "192", "193", "194", "195", "196", "197", "198", "199", "200", "201", "202", "203", "204", "205", "206", "207", "208", "209", "210", "211", "212", "213", "214", "215", "216", "217", "218", "219", "220", "221", "222", "223", "224", "225", "226", "227", "228", "229", "230", "231", "232", "233", "234", "235", "236", "237", "238", "239", "240", "241", "242", "243", "244", "245", "246", "247", "248", "249", "250", "251", "252", "253", "254", "255"]
    if color_code in valid_color_codes:
        return f"\033[{color_code}m{text}\033[0m"
    else:
        raise ValueError("Invalid ANSI color code.")

def get_terminal_size():
    try:
        return os.get_terminal_size().columns
    except OSError:
        return 80

def colorize(text, color_code):
    return "\033[{}m{}\033[0m".format(color_code, text)

color_codes = {
    "title_color": "1;35",  # Bright Magenta
    "section_title_color": "1;34",  # Bright Blue
    "content_color": "0;37",  # White
    "command_color": "1;32"  # Bright Green
}

def generate_full_dynamic_colored_interface(menu_title, left_panel_details, right_panel_commands):
    """
    Generate a full-system, dynamic, and colored CLI interface template.
    Adjusts to the window size and includes detailed ASCII art and functionalities.
    """
    columns = get_terminal_size()

    # Header and Footer
    top_border = colorize("=" * columns, color_codes["content_color"])
    title_row = colorize(f"{menu_title.center(columns)}", color_codes["title_color"])
    separator = colorize("=" * (columns - 2), color_codes["content_color"])

    # Left Panel
    left_panel = []
    for title, content in left_panel_details.items():
        left_panel.append(colorize(f"| {title.ljust(columns // 2 - 4)}", color_codes["section_title_color"]))
        left_panel.append(colorize(f"| {content.ljust(columns // 2 - 4)}\n", color_codes["content_color"]))
    left_panel = '\n'.join(left_panel)

    # Right Panel Commands
    right_panel = []
    for command, description in right_panel_commands.items():
        cmd_text = f"{command} - {description}"
        right_panel.append(colorize(f"| {cmd_text.ljust(columns // 2 - 4)}\n", color_codes["command_color"]))
    right_panel = '\n'.join(right_panel)

    # Combine Panels
    panels = []
    left_lines = left_panel.strip().split('\n')
    right_lines = right_panel.strip().split('\n')
    max_lines = max(len(left_lines), len(right_lines))
    for i in range(max_lines):
        left_line = left_lines[i] if i < len(left_lines) else " " * (columns // 2 - 2)
        right_line = right_lines[i] if i < len(right_lines) else " " * (columns // 2 - 2)
        panels.append(f"{left_line}{right_line}")
    panels = '\n'.join(panels)

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
