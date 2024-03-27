from datetime import datetime


def live_ascii_clock():
    # Get current time
    now = datetime.now()

    # Format time and date
    hour = now.strftime("%I")
    minute = now.strftime("%M")
    day = now.strftime("%d")
    month_year = now.strftime("%m/%y")

    # Construct the ASCII art for the clock
    clock_art = f"""
    Hr.     Min.    Dy.     Mn/Yr.
  .----.  .----.  .----.  .--------.  
  | {hour} | : | {minute} |  | {day} |  | {month_year} |  
  '----'  '----'  '----'  '--------'  
    """

    return clock_art


# Display the live ASCII clock
print(live_ascii_clock())

