import os
import shelve

SHELVE_DB = "shelve.db"


def nest_basket():
    """
    Logic: A master list, or 'nest', of all stored commands and files in the Nightjar CLI library.
    SYNTAX: [𝙉]=('input_parameter')
    PLAIN TEXT FORMAT: nest --input_parameter # parser should convert [nest] to [𝙉]
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
    except Exception as e:
        print(f"An error occurred: {str(e)}")


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


def discard_nest(param):
    """
    Logic: A command to delete a file saved in the nest library.
    CLI DISPLAY: Deletes a file saved in the nest library.
    ADDITIONAL REQ: nest commands must include the format of the file in the title.
    if the user confirms the remove_nest command with '-+' prior or during execution, skip confirmation prompt.
    SYNTAX: [-]=('nest_name.txt') # All nest  commands must include the format of the file in the title.
    PLAIN TEXT FORMAT: nest discard --nest_name.txt

    :param param: The name of the file to be deleted.
    :return: None
    """
    os.remove(f"nightjar_commands.db/{param}")
    print(f"Nest is Discarded! '{param}' is deleted.")