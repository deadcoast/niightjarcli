from datetime import datetime


CLOCK_ART_TEMPLATE = """Hr.     Min.    Dy.     Mn/Yr.
.----.  .----.  .----.  .--------.
| {hour} | : | {minute} |  | {day} |  | {month_year} |
'----'  '----'  '----'  '--------'"""

def live_ascii_clock():
    """
    Print an ASCII art representation of the current time.

    Returns:
        str: The ASCII art representation of the current time.
    """
    now = datetime.now()
    hour = now.strftime("%H")
    minute = now.strftime("%M")
    day = now.strftime("%d")
    month_year = now.strftime("%B %Y")
    CLOCK_ART_TEMPLATE = """Hr.     Min.    Dy.     Mn/Yr.
    .----.  .----.  .----.  .--------.
    | {hour} | : | {minute} |  | {day} |  | {month_year} |
    '----'  '----'  '----'  '--------'"""
    clock_art = CLOCK_ART_TEMPLATE.format(hour=hour, minute=minute, day=day, month_year=month_year)
    return clock_art


# Display the live ASCII clock
print(live_ascii_clock())

