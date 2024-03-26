import os
import shelve

SHELVE_DB = "shelve.db"

def basket(command_title, context):
    """
    Logic: SERVES AS THE --all argument. For result based options, it will refresh the current commands for --all .
    Example: eggs rotten --all. Useful for "delete all rotten eggs" command.
    SYNTAX: [𝘉]=('input_parameter')
    TEXT FORMAT: egg -rotten --all # parser should convert [basket] to [𝘉]
    :param command_title: basket "option" or "category"
    :param context:
    :return:
    """
def egg_list():
    """
    MENU: A master list, or 'nest', of all stored commands and files in the Nightjar CLI library.
    CATEGORICAL file LISTING SUBMENU: Displays egg files by sorted category.
    EXAMPLE:
    list TYPE TOTAL: Displays the file type and total number of files in the nest library.
    list BY TYPE: Displays the egg file titled followed by their file type.
    SEARCH EGG: Search for a specific egg file in the nest library.
    """
    for file in os.listdir("nightjar_commands.db"):
        print(file)
    # Placeholder: Add logic to display all files saved in the Nightjar CLI library.
    print("Eggs are ready to hatch!")


def find_egg():
    """
    MENU: A master list, or 'nest', of all stored commands and files in the Nightjar CLI library.
    CATEGORICAL file LISTING SUBMENU: Displays egg files by sorted category.
    list TYPE TOTAL: Displays the file type and total number of files in the nest library.
    list BY TYPE: Displays the egg file titled followed by their file type.
    SEARCH EGG: Search for a specific egg file in the nest library.
    """
    for file in os.listdir("nightjar_commands.db"):
        print(file)
    # Placeholder: Add logic to display all files saved in the Nightjar CLI library.
    print("Eggs are ready to hatch!")

def find_egg_by_type(file_type):
    """
    MENU: A master list, or 'nest', of all stored commands and files in the Nightjar CLI library.
    CATEGORICAL file LISTING SUBMENU: Displays egg files by sorted category.
    list TYPE TOTAL: Displays the file type and total number of files in the nest library.
    list BY TYPE: Displays the egg file titled followed by their file type.
    SEARCH EGG: Search for a specific egg file in the nest library.
    """
    for file in os.listdir("nightjar_commands.db"):
        if file.endswith(file_type):
            print(file)
    # Placeholder: Add logic to display all files saved in the Nightjar CLI library by file type.
    print("Eggs are ready to hatch!")

def find_egg_by_name(file_name):
    """
    MENU: A master list, or 'nest', of all stored commands and files in the Nightjar CLI library.
    CATEGORICAL file LISTING SUBMENU: Displays egg files by sorted category.
    list TYPE TOTAL: Displays the file type and total number of files in the nest library.
    list BY TYPE: Displays the egg file titled followed by their file type.
    SEARCH EGG: Search for a specific egg file in the nest library.
    """
    for file in os.listdir("nightjar_commands.db"):
        if file == file_name:
            print(file)
    # Placeholder: Add logic to display a specific file saved in the Nightjar CLI library.
    print("Egg is ready to hatch!")

def find_egg_by_size(file_size):
    """
    MENU: A master list, or 'nest', of all stored commands and files in the Nightjar CLI library.
    CATEGORICAL file LISTING SUBMENU: Displays egg files by sorted category.
    list TYPE TOTAL: Displays the file type and total number of files in the nest library.
    list BY TYPE: Displays the egg file titled followed by their file type.
    SEARCH EGG: Search for a specific egg file in the nest library.
    """
    for file in os.listdir("nightjar_commands.db"):
        if os.path.getsize(f"nightjar_commands.db/{file}") == file_size:
            print(file)
    # Placeholder: Add logic to display all files saved in the Nightjar CLI library by file size.
    print("Eggs are ready to hatch!")

def find_egg_by_path(file_path):
    """
    MENU: A master list, or 'nest', of all stored commands and files in the Nightjar CLI library.
    CATEGORICAL file LISTING SUBMENU: Displays egg files by sorted category.
    list TYPE TOTAL: Displays the file type and total number of files in the nest library.
    list BY TYPE: Displays the egg file titled followed by their file type.
    SEARCH EGG: Search for a specific egg file in the nest library.
    """
    for file in os.listdir("nightjar_commands.db"):
        if file_path in file:
            print(file)
    # Placeholder: Add logic to display all files saved in the Nightjar CLI library by file path.
    print("Eggs are ready to hatch!")


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

def rotten_egg(file_name):
    """
    Logic: A command to delete a file saved in the nest library.
    SYNTAX: [-]=('file_name')
    PLAIN TEXT FORMAT: egg -rotten --file_name
    MENU: A LIST OF THE EGG, THE SIZE OF THE EGG, THE FILE FORMAT OF THE EGG, THE PATH OF THE EGG.
    ADDITIONAL REQ: rotten eggs must provide a confirmation prompt before deletion.
    if the user confirms the remove_egg command with '-+' prior or during execution, skip confirmation prompt.
    CLI DISPLAY: tossed the stinky boi, .
    """
    os.remove(f"nightjar_commands.db/{file_name}")
    print(f"Egg is Discarded! '{file_name}' is deleted.")
    # Placeholder: Add logic to delete a file saved in the nest library.

