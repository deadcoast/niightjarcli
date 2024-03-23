#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2022-11-22
@Author: Firstname Lastname
@Title: nightjar - A Python CLI Nest Library
@Description: A Dynamic, customizable and modular CLI creation and Native Windows Library CLI.
@Features:  1. nest: The nightjar CLI home Library.
            2. twig: Command functions.
            3. egg: File specific commands and customizations.
            3. chirp: creat a simple print and validation command for the nightjars chirp language prompting to user.
            4. flight: Navigational menu: create new navigational menu's, hotkeys, list current flight plans.
            5. padding: A list of templates for storing user commands and files in 3 categories.
@Version: 0.1.0
@License: MIT
"""

import time
import shelve

import os
import sys

SHELVE_DB = "nightjar"
# The path to shelve database
def intro():
    # Intro function represents CLI initiation
    print("Welcome to the Nightjar CLI.")
    print("Type 'intro' to start the CLI.")
    print("Type 'exit' to quit the CLI.")

    # Command prompt
    command = input("> ")

    if command.lower() == 'intro':
        print("Nightjar CLI is active.")
    elif command.lower() == 'exit':
        print("Nightjar CLI is shutting down.")
        sys.exit()
    else:
        print("Invalid command. Please try again.")
        intro()

# Command prompt
command = input("> ")

# BANNER ASCII
#
#
#
#                                              /
#                                             /
#                                            /
#                                           /
#                                          /
#                                         /;
#                                        /;
#                                       //
#                                      //
#                                     ;/
#                                   ,//
#                               _,-' ;_,,
#                            _,'-_  ;|,'
#                        _,-'_,..--. |
#                ___   .'-'_)'  ) _)\|      ___
#              ,'"""`'' _  )   ) _)  ''--'''_,-'
#           -={-o-  /|    )  _)  ) ; '_,--''
#              \ -' ,`.  ) .)  _)_,''|
#               `."(   `------''     /
#                 `.\             _,'
#                   `-.____....-\\
#                             || \\
#                             // ||
#                            //  ||
#                           //   ||
#                       _-.//_, _||_,
#                         ,'   ,-'/
#
# ------------------------------------------------
# Thank you for visiting https://asciiart.website/
# This ASCII pic can be found at
# https://asciiart.website/index.php?art=animals/birds%20(land)

def intro():
    # Intro function represents CLI initiation
    print(f"`   \\     Welcome to nightjar CLI`")
    print(f"`   (o>    LOCATION: nest Library`")
    print(f"`   (()    1. intro to nightjar.`")
    print(f"`-- || ----2. help.`")
    print(f"`          3. list nightjar menu categories.`")
    print("Type 'exit' at anytime to quit the CLI.`")

    # Command prompt
    command = input("> ")

    if command.lower() == 'intro':
        print("Nightjar CLI is active.")

    elif command.lower() == 'exit':
        print("Nightjar CLI is shutting down.")
        sys.exit()
    else:
        print("Invalid command. Please try again.")
        intro()

def all_nest():
    """
    Lists all commands/files stored in the library with up to the first 50 characters of details.
    Lists details such as size and last modification time of the database file.
    """
    database_path = f"{SHELVE_DB}.dat"  # Shelve uses the .dat extension for the database file
    try:
        with shelve.open(SHELVE_DB, flag='r') as db:  # 'r' for read-only because we are listing
            print("Listing all stored items with details:")
            for key in db:
                item_preview = str(db[key])[
                               :50]  # Converts any type of item to a string and takes the first 50 characters
                print(f"{key}: {item_preview}...")
        # Gathering detailed information about the database file itself
        file_size = os.path.getsize(database_path)
        mod_time = os.path.getmtime(database_path)
        print(f"Library database file: {database_path}")
        print(f"Size: {file_size} bytes")
        print(f"Last Modified: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(mod_time))}")
    except FileNotFoundError:
        print("The storage database file does not exist.")


def initiate_nightjar(*args):
    """
    The actual startup logic when the 'intro' command is executed.
    """
    print("Nightjar CLI is active.")
    # [TODO] Add any necessary startup procedures here.


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


# More likely, this would be done through a batch file or a configured PATH environment variable.

def parse_cli_input(cli_input):
    if cli_input.startswith("-=-"):
        handle_command(cli_input[3:])
    else:
        handle_command(cli_input)


def handle_custom_syntax(command):
    # Mapping capital letters to custom symbols
    symbol_map = {'LL': '𝓁', 'TT': '𝑡', 'FF': 'ƒ'}
    for key, value in symbol_map.items():
        command = command.replace(key, value)
    parse_cli_input(command)  # Assuming parse_cli_input is a previously defined function


def view_cheat_sheet():
    # Assumed function to fetch and display CLI help content
    print("Displaying cheat sheet...")


# Template Library Placeholder
# Introduce a basic structure for future implementation of a template library using FileSystem-based methods.
def padding_nest():
    """
    Logic: A list of templates, or 'padding' in the Nightjar CLI library.
    CATEGORIES: 1. chirp padding (pad_chirp: A list of templates for nightjars chirp language prompting to user.
                    1. print to user.
                    2. print to user with input.
                    3. print to user with input and validation.
                2. twig padding: A list of templates for command functions.
                    1. create a new flight plan navigational menu.
                    2. create a new twig command.
                    3. create a new save egg file format for the nest.
                3. nest padding: A list of templates for storing user commands and files.
    UNIVERSAL: A master list, or 'nest', of all stored commands and files in the Nightjar CLI library.
    ADDITIONAL REQ: Nest commands must include the format of the file in the title.
    """
    if not os.path.exists("padding"):
        os.makedirs("padding")
    template_dir = "padding"
    if not os.path.exists(template_dir):
        os.makedirs(template_dir)  # Establish the directory structure for templates
    print("Padding nest created, lets add some twigs!.")

def pad_chirp("input_parameter"):
    """
    Logic: A list of templates, or 'padding' in the Nightjar CLI library.
    CATEGORIES: 1. chirp padding (pad_chirp): A list of templates for nightjars chirp language prompting to user.
                    1. print to user.
                    2. print to user with input.
                    3. print to user with input and validation.
                2. twig padding: A list of templates for command functions.
                    1. create a new flight plan navigational menu.
                    2. create a new twig command.
                    3. create a new save egg file format for the nest.
                3. nest padding: A list of templates for storing user commands and files.
    UNIVERSAL: A master list, or 'nest', of all stored commands and files in the Nightjar CLI library.
    ADDITIONAL REQ: Nest commands must include the format of the file in the title.
    """
    if not os.path.exists("padding"):
        os.makedirs("padding")
    template_dir = "padding"
    if not os.path.exists(template_dir):
        os.makedirs(template_dir)  # Establish the directory structure for templates
    print("Padding chirp created, lets add some chirps!.")
def bird_verbs(command_input, show_twig=None):
    """
    Parses and executes a given command_input by delegating to the appropriate function.
    """
    command_actions = {
        'store nest': store_nest,
        'store egg': store_egg,
        'store twig': store_twig,
        'get twig': get_twig,
        'get egg': get_egg,
        'get nest': get_nest,
        'show eggs': show_eggs,
        'show nest': all_nest,
        'show twig': show_twig,
        'discard twig': discard_twig(),
        'discard egg': discard_egg(),
        'discard nest': discard_nest(),
        'flight': flight_plan,
        'padding': padding_nest,
        'pad chirp': pad_chirp,
        'pad twig': pad_twig,
        'pad egg': pad_egg,
        # Add future command mappings here...
    }
    if parts := command_input.split():
        command_key, *args = parts
        if command_key in command_actions:
            command_actions[command_key](*args)
        else:
            get_twig(command_input)
    else:
        print("No twig entered.")


def get_egg(file_name):
    """
    Logic: a command to load and display a filed saved in the nest library.
    CLI DISPLAY: Loads and Displays the file contents in the CLI for the user.
    ADDITIONAL REQ: egg commands must include the format of the file in the title.
    """
    with open(f"nightjar_commands.db/{file_name}") as f:
        print(f"{file_name}\n{f.read()}")
        print(f"Egg is Hatching! '{file_name}' is ready.")
    # Placeholder: Add logic to load and display the file contents in the CLI for the user.


def lay_egg(file_name, file_content):
    """
    Logic: A command to save a file to the nest library.
    CLI DISPLAY: Saves a file to the nest library.
    ADDITIONAL REQ: egg commands must include the format of the file in the title.
    """
    if not os.path.exists("nightjar_commands.db"):
        os.makedirs("nightjar_commands.db")
    if not os.path.exists("nightjar_commands.db"):
        os.makedirs("nightjar_commands.db")  # Establish the directory structure for the nest library
    with open(f"nightjar_commands.db/{file_name}", 'w') as f:
        f.write(file_content)
        print(f"Egg is Laid! '{file_name}' is saved.")
    # Placeholder: Add logic to save the file to the nest library.


def show_eggs():
    """
    MENU: A master list, or 'nest', of all stored commands and files in the Nightjar CLI library.
    CATEGORICAL file LISTING SUBMENU: Displays egg files by sorted category.
    SHOW TYPE TOTAL: Displays the file type and total number of files in the nest library.
    SHOW BY TYPE: Displays the egg file titled followed by their file type.
    SEARCH EGG: Search for a specific egg file in the nest library.
    """
    for file in os.listdir("nightjar_commands.db"):
        print(file)
    # Placeholder: Add logic to display all files saved in the Nightjar CLI library.
    print("Eggs are ready to hatch!")

def rotten_egg(file_name):
    """
    Logic: A command to delete a file saved in the nest library.
    SYNTAX: [-]=('file_name')
    PLAIN TEXT FORMAT: egg discard --file_name
    MENU: A LIST OF THE EGG, THE SIZE OF THE EGG, THE FILE FORMAT OF THE EGG, THE PATH OF THE EGG.
    ADDITIONAL REQ: rotten eggs must provide a confirmation prompt before deletion.
    if the user confirms the remove_egg command with '-+' prior or during execution, skip confirmation prompt.
    CLI DISPLAY: tossed the stinky boi, .
    """
    os.remove(f"nightjar_commands.db/{file_name}")
    print(f"Egg is Discarded! '{file_name}' is deleted.")
    # Placeholder: Add logic to delete the file from the nest library.

def store_nest(command_title, context):
    """
    Logic: A master list, or 'nest', of all stored commands and files in the Nightjar CLI library.
    UNIVERSAL SAVE: Saves a command or file with context to the Nightjar CLI library.
    ADDITIONAL REQ: store_nest titles must include the format the file is to be saved in. it save.txt
    command_title VARIABLES LIST: .md, .asciidoc, .ansi, .txt, .json, .py, .sh, .csv, .html, .css, .js, .sql, .xml, .yaml,
    .toml, .ini, .cfg, .conf, .log, .md, .rst, .tex, .pdf, .docx, .pptx, .xlsx, .csv, .zip, .tar, .gz, .7z, .rar, .jpg,
    .png, .gif, .svg, .mp4, .mp3, .wav, .flac, .ogg, .avi, .mov, .mkv, .wmv, .webm, .flv, .pdf, .docx, .pptx, .xlsx,
    """
    with shelve.open('nightjar_commands.db') as db:
        db[command_title] = context
        print(f"Saved '{command_title}' to the library.")
    # Placeholder: Add logic to save a command or file with context to the Nightjar CLI library.
    """
    Saves a command or file with context to the Nightjar CLI library.
    """
    with shelve.open('nightjar_commands.db') as db:
        db[command_title] = context
        print(f"Saved '{command_title}' to the library.")
    # Placeholder: Add logic to save a command or file with context to the Nightjar CLI library.


def get_nest(command_title):
    """
    Logic: A master list, or 'nest', of all stored commands and files in the Nightjar CLI library.
    UNIVERSAL EXECUTE:Retrieves a command or file from the Nightjar CLI library.
    """
    with shelve.open('nightjar_commands.db') as db:
        if context := db.get(command_title):
            print(f"Retrieved '{command_title}' from the library: {context}")
        else:
            print(f"Command '{command_title}' not found in library.")


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


# Continue with the rest of the CLI code...
def discard_twig(command_title):
    """
    COMMAND ONLY: Deletes a 'twig' command stored in the Nightjar CLI library nest,
    @nightjar FORMAT: [−−]=('command_title')
    PLAIN TEXT FORMAT: twig discard --command_title
    if the user confirms the remove_twig command with '-+' prior or during execution, skip confirmation prompt.
    """
    print(f"Deleting '{command_title}' from the library.")
    # Check if the user has already confirmed the deletion
    if '-+' in sys.argv:
        print("User has already confirmed deletion.")
    else:
        # Ask for confirmation before deletion
        if require_confirmation(f"Are you sure you want to delete '{command_title}'?"):
            # Perform the deletion operation here.
            print(f"Deleted '{command_title}' from the library.")
        else:
            print("Deletion cancelled.")


def get_twig(task_name, *args):
    """
    Starts and or simulates a task or twig with a given task_name and additional arguments.
    This is an enhancement over the placeholder that provides actual logic.
    """
    # Example logic to start a task; this would be replaced with actual actions for each task.
    print(f"twig successfully grabbed from nest: {task_name}")
    # Perform the task start operation here, for instance:
    # Run a script, execute a command, start a new process, etc.
    print(f"twig '{task_name}' started with arguments {args}.")

def store_twig(task_name, task_description):
    """
    Logic:  A specific logic for saving operational twig python commands to the Nightjar CLI Nest. the twig command is
            designed as the command the directly edits and or enhances the nightjar CLI with new commands.
    PADDING: simple twig commands can be created through the padding nest.
    DIRECT INJECTION: nightjar CLI can create simple prompting and validation twig commands to incorporate directly
                      into the CLI. The twig commands can be stored into nightjars functions, workflows and nest.
                      On the next CLI restart, the nightjar CLI will be updated with the new twig command.
    AUTOMATIC SAVE: twig commands are automatically saved with the proper .py format.
    """
    with shelve.open('nightjar_commands.db') as db:
        db[task_name] = task_description
        print(f"Saved '{task_name}' to the library.")
    # Placeholder: Add logic to save a command or file with context to the Nightjar CLI library.
    """
    Saves a command or file with context to the Nightjar CLI Nest library.
    """
    with shelve.open('nightjar_commands.db') as db:
        db[task_name] = task_description
        print(f"Saved '{task_name}' to the library.")
    # Placeholder: Add logic to save a command or file with context to the Nightjar CLI functions.
    """
    Creates and saves a simple prompting and validation twig command to the Nightjar CLI functions.
    """


# Navigation function, provide a list of 4 available menus to navigate to
def flight_plan(menu_name, *args):
    print(f"`   \\      Where to: {menu_name}")
    print(f"`   (o>     Where to: {get_twig(menu_name)}")
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
        all_nest()
    elif menu_name == 'twig':
        get_twig(menu_name)
    elif menu_name == 'flight':
        flight_plan(menu_name)


def parse_nightjar(command):
    """
    Parse and execute commands within the @nightjar CLI.
    """
    if command.startswith("ƒ="):
        # Logic for if command
        pass
    elif command.startswith("[+]="):
        store_nest(command[4:], )
    elif command.startswith("[-]="):
        discard_twig(command[4:])
    elif command.startswith("[-+]="):
        get_twig(command[5:])
    elif command.startswith("[%]="):
        flight_plan(command[4:])
    elif command.startswith("[𝓁]="):
        show_eggs()
    elif command.startswith("[𝑡]="):
        template_placeholder()


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
            command = input("> ")
            if command.lower() == 'exit':
                break
            elif command.startswith(":"):
                handle_multiline_command(command)
            else:
                parse_nightjar(command)


if __name__ == "__main__":
    intro()
    template_library_structure()
    initiate_nightjar()
    main()


def main_loop():
    welcome_message = "Welcome to @nightjar CLI. Type 'exit' to quit."
    print(welcome_message)

    while True:
        command_input = input("nightjar> ")
        if command_input.lower() == 'exit':
            break
        elif command_input.startswith("-=-"):
            handle_command(command_input[3:])
        else:
            handle_command(command_input)

# This logic would be below the intro() function within the `if __name__ == "__main__":` block.
