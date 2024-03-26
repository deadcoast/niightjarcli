import os
import shelve
from datetime import time

SHELVE_DB = "shelve.dat"


def padding_nest():
    """
    SYNTAX: [𝙉],[𝘗]=('input_parameter')
    PLAIN TEXT FORMAT: nest -pp --input_parameter # parser should convert [pp] to [𝘗]
    Logic: A list of templates, or 'padding' in the Nightjar CLI library.
    CATEGORIES:
    :param: (pad_chirp): A list of templates for nightjars chirp language prompting and validation to user.
    :param: (pad_twig): A list of templates for placeholder command functions.
    :param: (pad_nest): A list of templates for structuring files in the nightjar CLI nest Library.
    :param: (pad_egg): A list of templates for creating egg files.
    :param: (pad_flight): A list of templates for creating navigational menu maps aka "flight plans".
    :param: MENU: A list of function VARIABLES:
                    1. print to user.
                    2. print to user with input.
                    3. print to user with input and validation.
    """
    if not os.path.exists("padding"):
        os.makedirs("padding")
    template_dir = "padding"
    if not os.path.exists(template_dir):
        os.makedirs(template_dir)  # Establish the directory structure for templates
    print("Padding nest created, lets add some twigs!.")


def padding_egg():
    """
    Logic: A list of templates for creating egg files in the Nightjar CLI library.
    CATEGORIES:
    :param: (egg_chirp): A list of templates for nightjars chirp language prompting and validation to user.
    :param: (egg_twig): A list of templates for placeholder command functions.
    :param: (egg_nest): A list of templates for structuring files in the nightjar CLI nest Library.
    :param: (egg_egg): A list of templates for creating egg files.
    :param: (egg_flight): A list of templates for creating navigational menu maps aka "flight plans".
    :param: MENU: A list of function VARIABLES:
                    1. print to user.
                    2. print to user with input.
                    3. print to user with input and validation.
    """
    if not os.path.exists("egg"):
        os.makedirs("egg")
    template_dir = "egg"
    if not os.path.exists(template_dir):
        os.makedirs(template_dir)  # Establish the directory structure for templates
    print("Egg nest created, lets add some eggs!.")


def padding_twig():
    """
    Logic: A list of templates for creating twig commands in the Nightjar CLI library.
    CATEGORIES:
    :param: (twig_chirp): A list of templates for nightjars chirp language prompting and validation to user.
    :param: (twig_twig): A list of templates for placeholder command functions.
    :param: (twig_nest): A list of templates for structuring files in the nightjar CLI nest Library.
    :param: (twig_egg): A list of templates for creating egg files.
    :param: (twig_flight): A list of templates for creating navigational menu maps aka "flight plans".
    :param: MENU: A list of function VARIABLES:
                    1. print to user.
                    2. print to user with input.
                    3. print to user with input and validation.
    """
    if not os.path.exists("twig"):
        os.makedirs("twig")
    template_dir = "twig"
    if not os.path.exists(template_dir):
        os.makedirs(template_dir)  # Establish the directory structure for templates
    print("Twig nest created, lets add some twigs!.")


def padding_flight():
    """
    Logic: A list of templates for creating navigational menu maps aka "flight plans" in the Nightjar CLI library.
    CATEGORIES:
    :param: (flight_chirp): A list of templates for nightjars chirp language prompting and validation to user.
    :param: (flight_twig): A list of templates for placeholder command functions.
    :param: (flight_nest): A list of templates for structuring files in the nightjar CLI nest Library.
    :param: (flight_egg): A list of templates for creating egg files.
    :param: (flight_flight): A list of templates for creating navigational menu maps aka "flight plans".
    :param: MENU: A list of function VARIABLES:
                    1. print to user.
                    2. print to user with input.
                    3. print to user with input and validation.
    """
    if not os.path.exists("flight"):
        os.makedirs("flight")
    template_dir = "flight"
    if not os.path.exists(template_dir):
        os.makedirs(template_dir)  # Establish the directory structure for templates
    print("Flight nest created, lets add some flight plans!.")


def padding_chirp():
    """
    Logic: A list of templates for creating chirp commands in the Nightjar CLI library.
    CATEGORIES:
    :param: (chirp_chirp): A list of templates for nightjars chirp language prompting and validation to user.
    :param: (chirp_twig): A list of templates for placeholder command functions.
    :param: (chirp_nest): A list of templates for structuring files in the nightjar CLI nest Library.
    :param: (chirp_egg): A list of templates for creating egg files.
    :param: (chirp_flight): A list of templates for creating navigational menu maps aka "flight plans".
    :param: MENU: A list of function VARIABLES:
                    1. print to user.
                    2. print to user with input.
                    3. print to user with input and validation.
    """
    if not os.path.exists("chirp"):
        os.makedirs("chirp")
    template_dir = "chirp"
    if not os.path.exists(template_dir):
        os.makedirs(template_dir)  # Establish the directory structure for templates
    print("Padding up the nest, lets add some twigs to structure!.")

def padding_basket(command_title, contex):
    """
    Logic: A master list, or 'padding', of all stored commands and files in the Nightjar CLI library.
    SYNTAX: [𝙉]=('input_parameter')
    PLAIN TEXT FORMAT: padding --input_parameter # parser should convert [padding] to [𝙉]
    Lists all commands/files stored in the library with up to the first 50 characters of details.
    Lists details such as size and last modification time of the database file.
    :param command_title: 
    :param contex: 
    :param command_title: basket "option" or "category"
    :param context: a list of commands or files stored in the library with up to the first 50 characters of details.
    :param command_title: basket "option" or "category"
    :param context: a list of commands or files stored in the library with up to the first 50 characters of details.
    :return: padding_basket
    """
    database_path = f"{SHELVE_DB}.dat"  # Shelve uses the .dat extension for the database file
    try:
        basket_float_padding(database_path)
    except FileNotFoundError:
        print("The storage database file does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    return padding_basket


def basket_float_padding(database_path):
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

def store_padding(command_title, context):
    """
    Logic: A list of templates for creating chirp commands in the Nightjar CLI library.
    :param: (chirp_chirp): A list of templates for nightjars chirp language prompting and validation to user.
    :param: (chirp_twig): A list of templates for placeholder command functions.
    :param: (chirp_nest): A list of templates for structuring files in the nightjar CLI nest Library.
    :param: (chirp_egg): A list of templates for creating egg files.
    :param: (chirp_flight): A list of templates for creating navigational menu maps aka "flight plans".
    """
    with shelve.open(SHELVE_DB, flag='c') as db:
        db[command_title] = context
        print(f"Saved '{command_title}' to the library.")
    return store_padding

def get_padding(command_title):
    """
    Logic: A master list, or 'padding', of all stored commands and files in the Nightjar CLI library.
    UNIVERSAL EXECUTE:Retrieves a command or file from the Nightjar CLI library.
    """
    with shelve.open(SHELVE_DB) as db:
        if context := db.get(command_title):
            print(context)
    return get_padding

def lay_padding(file_name, file_content):
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
    return lay_padding