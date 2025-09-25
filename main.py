# main.py

import shutil
from pathlib import Path
import time

# You can easily manage file extensions and their target folders here.
FILE_EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".tiff"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".webm", ".flv"],
    "Audio": [".mp3", ".wav", ".flac", ".aac"],
    "Documents": [".pdf", ".docx", ".xlsx", ".pptx", ".txt", ".csv", ".doc"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Applications": [".exe", ".msi", ".apk"],
    "Other": []
}

def get_unique_filepath(destination: Path, filename: str) -> Path:
    """If a file with the same name exists at the destination, appends a number like (1), (2), etc."""
    counter = 1
    new_filepath = destination / filename
    while new_filepath.exists():
        new_filepath = destination / f"{Path(filename).stem}({counter}){Path(filename).suffix}"
        counter += 1
    return new_filepath

def organize_folder(target_path: Path):
    """Organizes the specified directory based on the FILE_EXTENSIONS mapping."""
    if not target_path.is_dir():
        print(f"Error: '{target_path}' is not a valid directory.")
        return

    print("-" * 40)
    print(f"Organizing files in '{target_path.name}'...")
    
    for folder_name in FILE_EXTENSIONS.keys():
        (target_path / folder_name).mkdir(exist_ok=True)

    for item in target_path.iterdir():
        if item.is_file() and item.name != "main.py":
            moved = False
            for folder_name, extensions in FILE_EXTENSIONS.items():
                if item.suffix.lower() in extensions:
                    destination_folder = target_path / folder_name
                    new_filepath = get_unique_filepath(destination_folder, item.name)
                    shutil.move(str(item), str(new_filepath))
                    print(f"✓ Moved '{item.name}' -> '{folder_name}'")
                    moved = True
                    break # File moved, no need to check other categories.
            
            if not moved:
                destination_folder = target_path / "Other"
                new_filepath = get_unique_filepath(destination_folder, item.name)
                shutil.move(str(item), str(new_filepath))
                print(f"✓ Moved '{item.name}' -> 'Other'")

    print("\n✓ Organization complete!")
    print("-" * 40)


if __name__ == "__main__":
    default_path = Path.home() / "Downloads"
    
    print("Python File Organizer")
    print("=" * 25)
    
    user_input = input(f"Enter the path to organize (Default: {default_path}): ")

    target_directory = default_path if not user_input.strip() else Path(user_input)

    organize_folder(target_directory)
    time.sleep(4) # Prevents the console window from closing immediately.
