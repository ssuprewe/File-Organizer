# Python File Organizer

A simple yet powerful Python script that automatically organizes your Downloads folder or any other directory into categories in seconds.

---

## ✨ Features

*   **Automatic Path Detection**: Automatically suggests the user's "Downloads" folder as the default target.
*   **Flexible Usage**: Allows the user to specify any directory path for organization.
*   **Easily Customizable**: Adding new file types and categories is as simple as editing a single dictionary in the code.
*   **Handles Duplicates**: If a file with the same name already exists in the destination, it renames the new file (e.g., `document(1).pdf`) to prevent data loss.
*   **Cross-Platform**: Works seamlessly on Windows, macOS, and Linux thanks to Python's `pathlib`.
*   **Zero Dependencies**: Uses only Python's standard libraries, requiring no extra installations.

## 🚀 How to Use

1.  Clone this repository or simply download the `main.py` file.
2.  Open a terminal (Command Prompt, PowerShell, etc.) on your computer.
3.  Navigate to the directory where you saved `main.py` using the `cd` command.
4.  Run the script with the following command:
    ```sh
    python main.py
    ```
5.  The script will prompt you for a folder to organize.
    *   Press **Enter** to organize your default `Downloads` folder.
    *   Alternatively, type or paste a different folder path and then press **Enter**.

## 🔧 How to Customize

Adding new categories or file types is straightforward. Open `main.py` with any text editor and find the `FILE_EXTENSIONS` dictionary at the top.

For example, to add a new "Design" category for `.svg` and `.psd` files, you would modify the dictionary like this:

```python
# Part of the main.py file

FILE_EXTENSIONS = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".tiff"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv", ".webm", ".flv"],
    "Audio": [".mp3", ".wav", ".flac", ".aac"],
    "Documents": [".pdf", ".docx", ".xlsx", ".pptx", ".txt", ".csv", ".doc"],
    "Design": [".svg", ".psd", ".ai"], # <-- NEWLY ADDED LINE
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Applications": [".exe", ".msi", ".apk"],
    "Other": [] 
}
```
That's it! The next time you run the script, it will create a "Design" folder and move the corresponding files into it.
