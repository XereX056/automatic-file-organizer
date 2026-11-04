PREVIEW_ONLY = True
from pathlib import Path
import shutil
import argparse
import logging

logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Folder we want to organize
TARGET_FOLDER = Path("test_files")

# File extension categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".doc"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Archives": [".zip", ".rar", ".7z"],
}


def get_category(file):
    """Return the category for a file based on its extension."""
    extension = file.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_destination(destination):
    """Generate a unique filename if the destination already exists."""

    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = (
            f"{destination.stem}_{counter}"
            f"{destination.suffix}"
        )

        new_destination = destination.with_name(new_name)

        if not new_destination.exists():
            return new_destination

        counter += 1
def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Organize files by their extensions."
    )

    parser.add_argument(
        "folder",
        nargs="?",
        default="test_files",
        help="Folder to organize (default: test_files)."
    )

    parser.add_argument(
        "--move",
        action="store_true",
        help="Actually move files instead of previewing."
    )

    return parser.parse_args()

def organize_files():
    """Organize files into folders based on their extensions."""

    if not TARGET_FOLDER.exists():
        print(f"Error: The folder '{TARGET_FOLDER}' does not exist.")
        return

    if not TARGET_FOLDER.is_dir():
        print(f"Error: '{TARGET_FOLDER}' is not a folder.")
        return

    for file in TARGET_FOLDER.iterdir():

        if not file.is_file():
            continue

        category = get_category(file)
        destination_folder = TARGET_FOLDER / category
        destination = destination_folder / file.name
        destination = get_unique_destination(destination)

        try:
            if PREVIEW_ONLY:
                print(f"Would move: {file.name} -> {category}")
            else:
                destination_folder.mkdir(exist_ok=True)
                shutil.move(str(file), str(destination))
                print(f"Moved: {file.name} -> {category}")
                logging.info(f"Moved: {file.name} -> {category}")
        except OSError as error:
            print(f"Could not move {file.name}: {error}")
            logging.error(f"Could not move {file.name}: {error}")

if __name__ == "__main__":
    args = parse_arguments()
    TARGET_FOLDER = Path(args.folder)
    PREVIEW_ONLY = not args.move
    organize_files()
