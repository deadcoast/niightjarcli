import re
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# "Created on 2022-11-22
# "@Author: deadcoast
# "@Title: nightjar - A Python CLI Nest Library
# "@Description: A Dynamic, customizable and modular CLI creation and Native Windows Library CLI.
# "@Features:
# 1. nest: The nightjar CLI home Library.
# 2. twig: Command functions.
# 3. egg: File specific commands and customizations.
# 4. chirp: creat a simple print and validation command for the CLI menu.
# 5. flight: Navigational menu: create new navigational menu's, hotkeys, list current flight plans.
# 6. padding: A list of templates for storing user commands and files in 3 categories.
# @Version: 0.1.0
# @License: MIT
"""

import getpass
import logging
import os
import shelve
import sys
import time
from pathlib import Path

import self

from src.modules.egg_handler import lay_egg, get_egg, rotten_egg
from src.modules.nest_handler import get_nest
from src.modules.padding_handler import discard_nest, padding_egg, padding_flight, padding_chirp, padding_twig, \
    padding_nest, padding_basket
from src.modules.twig_handler import list_twigs, discard_twig, get_twigs, store_twig

# Command prompt
command = input("> ")
SHELVE_DB = "shelve.dat"

class NightjarCLILogging(object):
    def __init__(self):
        self.__DB_PATH = None
        self.__SHELVE_DB = None
        self.__setup_logging()
        self.__setup_database()

    def __setup_logging(self):
        logging.basicConfig(
            filename="nightjar.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        logging.info("Nightjar CLI is active.")

    def __setup_database(self):
        HOME_DIR = Path.home()
        self.__DB_PATH = HOME_DIR / ".nightjar"
        self.__DB_PATH.mkdir(parents=True, exist_ok=True)
        self.__SHELVE_DB = self.__DB_PATH / "nightjar"
        if not self.__SHELVE_DB.exists():
            with shelve.open(self.__SHELVE_DB):
                pass

    def execute_database_operations(self, key, value):
        try:
            with shelve.open(self.__SHELVE_DB) as db:
                db[key] = value
                logging.info('Value for the key is: %s', value)
        except FileNotFoundError as e:
            logging.error(f"Database does not exist: {str(e)}")
        except KeyError as e:
            logging.error(f"Key does not exist in the database: {str(e)}")
        except Exception as e:
            logging.error(f"Error accessing the database: {str(e)}")

    def run(self):
        self.execute_database_operations("key", "value")

if __name__ == "__main__":
    nightjar_cli_logging = NightjarCLILogging()
    nightjar_cli_logging.run()


# The path to shelve database
def intro():
    # Intro function represents CLI initiation
    print("`   \\     Welcome to nightjar CLI`")
    print("`   (o>    LOCATION: nest Library`")
    print("`   (()    1. intro to nightjar.`")
    print("`-- || ----2. help.`")
    print("`          3. list nightjar menu categories.`")
    print("Type 'exit' at anytime to quit the CLI.`")

    # Command prompt
    command = input("> ")

    if command.lower() == 'intro':
        print("nightjar CLI is active.")

    elif command.lower() == 'exit':
        print("nightjar CLI is shutting down.")
        sys.exit()
    else:
        print("Invalid command. Please try again.")
        intro()


# The path to shelve database
def header():
    """
    Header function represents CLI initiation
    """
    try:
        logging.error("Welcome to the Nightjar CLI.")
        logging.error("Type 'intro' to start the CLI.")
        logging.error("Type 'exit' to quit the CLI.")
    except Exception as e:  # Catch any exceptions that occur
        print(f"An error occurred: {str(e)}")
        return

    try:
        running = True
        while running:
            # Command prompt
            command = getpass.getpass("> ")

            command_lower = command.lower()
            if command_lower == 'intro':
                logging.error("Nightjar CLI is active.")
                running = False
            elif command_lower == 'exit':
                logging.error("Nightjar CLI is shutting down.")
                return
            else:
                logging.error("Invalid command. Please try again.")
    except Exception as e:  # Catch any exceptions that occur
        print(f"An error occurred: {str(e)}")
        return

    finally:
        print("Nightjar CLI is shutting down.")

ascii_art = None
# The path to shelve database
SHELVE_DB_PATH = Path.home() / "shelve.dat" / SHELVE_DB

class AsciiArtDisplay:
    def __init__(self, file_path):
        self.file_path = file_path
        self.ascii_art = None

    def display(self):
        if self.ascii_art is None:
            try:
                with open(self.file_path, 'r') as file:
                    self.ascii_art = file.read()
            except OSError as e:
                logging.error(f"The ASCII art file '{self.file_path}' is missing.")
                raise
            except PermissionError as e:
                raise PermissionError("Unable to read the ASCII art file due to permission issues.") from e
        return self.ascii_art or "No ASCII art found."

    # Define a function that converts users plain text to print("` `") format
    def ascii_header_canvas(self):
        """
        Logic: A function to convert a user's plain text to the nightjar CLI print format.
        """
        print("`####################################################")
        print("`#   \\     # Welcome to nightjar CLI               #`")
        print("`#   (o>    # LOCATION: {str(self.file_path)}       #`")
        print("`#   (()    # [1.] intro to nightjar                #`")
        print("`#-- || ----# [2.] help.                            #`")
        print("`# nightjar # [3.] list nightjar menu categories.   #`")
        print("`#   CLI    # Type 'exit' anytime to quit CLI.      #`")
        print("`####################################################")

def initiate_nightjar():
    """
    The actual startup logic when the 'intro' command is executed.
    """
    try:
        print("Nightjar CLI is active.")
        # [TODO] Add any necessary startup procedures here.
    except Exception as e:
        print(f'Error occurred: {str(e)}')


def handle_multiline_input():
    """
    Handles multi-line input from user, starting with [:]START and ending with [:]END.
    """
    print("Enter multi-line content. Terminate with [:]END.")
    input_lines = []
    while True:
        line = input()
        if line == "[:]END":
            break
        input_lines.append(line)
    return "\n".join(input_lines)


def handle_custom_syntax(command):
    """
    Replaces capital letters in the command with custom symbols.

    Args:
        command (str): The command to be processed.
    """
    if not isinstance(command, str):
        raise ValueError("Command must be a string.")
    
    # Mapping capital letters to custom symbols
    symbol_map = {'LL': '𝓁', 'TT': '𝑡', 'FF': 'ƒ'}
    for key, value in symbol_map.items():
        command = command.replace(key, value)
    
    try:
        bird_verbs(command)  # Assuming parse_cli_input is a previously defined function
    except Exception as e:
        print(f'Error occurred while executing bird_verbs: {str(e)}')
    
    return True


def view_cheat_sheet():
    # Assumed function to fetch and display CLI help content
    print("Displaying cheat sheet...")


def bird_verbs(command_input, nest_basket, discard_padding=None, *args):
    """
    Parses and executes a given command_input by delegating to the appropriate function.
    """
    command_actions = {
        'nest --all': nest_basket,
        '+nest': store_nest,
        '-rotten nest': discard_nest(command_input) if command_input else discard_nest("user_input.txt"),
        'get nest': get_nest(command_input),
        'lay egg': lay_egg(command_input) if command_input else lay_egg("user_input.txt", "user_input.txt"),
        ' egg --all': egg_list,
        'rotten egg': rotten_egg,
        'get egg': get_egg,
        'list twigs': list_twigs(command_input),
        '-rotten twig': discard_twig(command_input) if command_input else discard_twig("twig_1.py", ),
        'lay twig': store_twig,
        'get twig': get_twigs,
        'flight': flight_plan(command_input),
        '+flight': store_flight,
        '-rotten flight': discard_flight(command_input) if command_input else discard_flight("flight_1.py"),
        'get flight': get_flight,
        'chirp': chirp(command_input),
        'chirp --all': chirp_list,
        'discard chirp': discard_chirp,
        'get chirp': get_chirp,
        'get help': view_cheat_sheet,
        'intro': initiate_nightjar,
        'rotten padding': discard_padding,
        'padding --all': padding_basket,
        'padding': padding_nest,
        'pad egg': padding_egg(),
        'padding flight': padding_flight(),
        'padding chirp': padding_chirp(),
        'padding twig': padding_twig(),
        'help': view_cheat_sheet,
        'intro': initiate_nightjar,

        # Add future command mappings here...
    }
    if parts := command_input.split():
        command_key, *args = parts
        if command_key in command_actions:
            command_actions[command_key](*args)
        else:
            get_twigs(command_input)
    else:
        print("No twig entered.")


def require_confirmation(prompt):
    """
    Displays a confirmation prompt and returns True if the user confirms.
    @nightjar FORMAT: [-+]=(skip_confirmation_prompt)
    PLAIN TEXT FORMAT: twig discard --command_title -+skip
    """
    if not prompt.endswith('?'):
        prompt += '?'

    print(prompt, end=' ')
    if '-+' in input().lower():
        return True
    user_input = input(f"{prompt} (yes/no): ").strip().lower()
    return user_input in ['yes', 'y']


# Navigation function, provide a list of 4 available menus to navigate to
def flight_plan(menu_name, *args):
    print(f"`   \\      Where to: {menu_name}")
    print(f"`   (o>     Where to: {get_twigs(menu_name)}")
    print(f"`   (()     Where to: {get_nest}")
    print(f"`---||------Where to: {menu_name}")

    # Placeholder: Implement menu navigation logic here.
    print(f"Navigation to '{menu_name}' with arguments {args}.")
    # Placeholder: Add logic to navigate to the specified menu.
    # Add logic to navigate to the specified menu.
    # In this example, we'll just print the menu name again for demonstration purposes.
    print(f"Navigated to '{menu_name}'.")
    # Placeholder: Add logic to navigate to the specified menu.
    print(f"Navigation to '{menu_name}' with arguments {args}.")
    # Placeholder: Add logic to navigate to the specified menu.
    # Add logic to navigate to the specified menu.
    # In this example, we'll just print the menu name again for demonstration purposes.
    print(f"Navigated to '{menu_name}'.")
    # Placeholder: Add logic to navigate to the specified menu.
    if menu_name == 'main':
        initiate_nightjar()
    elif menu_name == 'nest':
        nest_list_all()
    elif menu_name == 'twig':
        get_twigs(menu_name)
    elif menu_name == 'flight':
        flight_plan(menu_name)


def rotten_flight(command):
    """
    SYNTAX: command_title[-r]=('command')
    PLAIN TEXT FORMAT: command -rotten --argument
    Logic: A command to delete an option, argument or file saved in the nest library.
    CLI DISPLAY: Deletes a command saved in the nest library.
    """
    with shelve.open(SHELVE_DB) as db:
        del db[command]
        print(f"Command '{command}' deleted from the library.")
    # Placeholder: Add logic to delete a command from the nest library.
    with shelve.open(SHELVE_DB) as db:
        del db[command]
        print(f"Command '{command}' deleted from the library.")
    # Placeholder: Add logic to delete a command from the nest library.


def store(command):
    """
    SYNTAX: [+]=('command')
    PLAIN TEXT FORMAT: +command --command_context
    Logic: A command to save a command to the nest library.
    CLI DISPLAY: Saves a command to the nest library.
    """
    with shelve.open(SHELVE_DB) as db:
        db['command'] = command
        print(f"Command '{command}' saved to the library.")
    # Placeholder: Add logic to save a command to the nest library.
    with shelve.open(SHELVE_DB) as db:
        db['command'] = command
        print(f"Command '{command}' saved to the library.")
    # Placeholder: Add logic to save a command to the nest library.


def twig(command):
    """
    SYNTAX: command_title[-]=('command')
    PLAIN TEXT FORMAT: command twig --command
    Logic: A command to delete a command saved in the nest library.
    CLI DISPLAY: Deletes a command saved in the nest library.
    """
    with shelve.open(SHELVE_DB) as db:
        del db[command]
        print(f"Command '{command}' deleted from the library.")
    # Placeholder: Add logic to delete a command from the nest library.
    with shelve.open(SHELVE_DB) as db:
        del db[command]
        print(f"Command '{command}' deleted from the library.")
    # Placeholder: Add logic to delete a command from the nest library.


def get(command):
    """
    SYNTAX: command_title[+]=('command')
    PLAIN TEXT FORMAT: command get --command
    Logic: A command to load a command saved in the nest library.
    CLI DISPLAY: Loads a command saved in the nest library.
    """
    with shelve.open(SHELVE_DB) as db:
        print(db[command])
    # Placeholder: Add logic to load a command from the nest library.
    with shelve.open(SHELVE_DB) as db:
        print(db[command])
    # Placeholder: Add logic to load a command from the nest library.


def rotten(command):
    """
    SYNTAX: command_title[-]=('command')
    PLAIN TEXT FORMAT: command discard --command
    Logic: A command to delete a command saved in the nest library.
    CLI DISPLAY: Deletes a command saved in the nest library.
    """
    with shelve.open(SHELVE_DB) as db:
        if command in db:
            del db[command]
            print(f"Command '{command}' deleted from the library.")
        else:
            print(f"Command '{command}' does not exist in the library.")
        # Placeholder: Add logic to delete a command from the nest library.
        if command in db:
            del db[command]
            print(f"Command '{command}' deleted from the library.")
        else:
            print(f"Command '{command}' does not exist in the library.")
        # Placeholder: Add logic to delete a command from the nest library.
    return True


def padding(command):
    """
    SYNTAX: command_title[𝙋]=('command')
    PLAIN TEXT FORMAT: command pad --command # pad will always parse to [𝙋]=command
    Logic: A command to save a command to the nest library.
    CLI DISPLAY: Saves a command to the nest library.
    """
    try:
        with shelve.open(SHELVE_DB) as db:
            db[command] = command
            print(f"Command '{command}' saved to the library.")
    except Exception as e:
        print(f"Error occurred while saving command: {e}")
    # Placeholder: Add logic to save a command to the nest library.
    try:
        with shelve.open(SHELVE_DB) as db:
            db[command] = command
            print(f"Command '{command}' saved to the library.")
    except Exception as e:
        print(f"Error occurred while saving command: {e}")
    # Placeholder: Add logic to save a command to the nest library.
    db.close()


def parse_nightjar(command):
    """
    Logic: The parsing logic and custom Syntax Translator for the nightjar next CLI Library.
    Parse and execute commands within the @nightjar CLI.
    """
    if not command.strip():
        raise ValueError("Invalid command. Please try again.")
    
    command_mapping = {
        "nightjar=-=-": native_init,
        "FF=ƒ": if_command,
        "[store]=+": store,
        "[discard]=-": rotten,
        "[pad]=𝙋": padding,
        "[LL]=𝙇": list,
        "[egg]=𝙀": padding_nest,
        "[get]=𝙂": get,
        "[TT]=𝙏": twig,
        "[nest]=𝙉": nest_list_all,
        "[flight]=menu": flight_plan
    }
    
    for prefix, func in command_mapping.items():
        if re.match(re.escape(prefix), command):
            if func.__name__ in globals() and callable(globals()[func.__name__]):
                func(command[len(prefix):])
            else:
                raise ValueError("Invalid command. Please try again.")
            return
    
    raise ValueError("Invalid command. Please try again.")


# Main CLI Loop

def main():
    if "-=-" in sys.argv:
        # Strip off the -=- and continue
        sys.argv = [cmd.replace("-=-", "") for cmd in sys.argv]
        # Command without -=- can be the first argument after the script name
        command = sys.argv[1] if len(sys.argv) > 1 else ""
        parse_nightjar(command)
    else:
        # If -=- is not present, enter interactive mode
        print("Welcome to @nightjar CLI. Type 'exit' to quit.")
        while True:
            command_input = input("nightjar> ")
            if command_input.lower() == 'exit':
                break
            elif command_input.startswith("-=-"):
                parse_nightjar(command_input[3:])
            else:
                parse_nightjar(command_input)

    print("Nightjar CLI is shutting down.")


if __name__ == "__main__":
    intro()
    lay_egg("egg_1.py", "This is the first egg.")
    lay_egg("egg_2.py", "This is the second egg.")
    lay_egg("egg_3.py", "This is the third egg.")
    lay_egg("egg_4.py", "This is the fourth egg.")
    padding_nest()
    initiate_nightjar(self)
    main()


def main_loop():
    welcome_message = "Welcome to @nightjar CLI. Type 'exit' to quit."
    print(welcome_message)

    while True:
        command_input = input("nightjar> ")
        if command_input.lower() == 'exit':
            break
        elif command_input.startswith("-=-"):
            handle_multiline_input(command_input[3:])
        else:
            handle_multiline_input(command_input)
