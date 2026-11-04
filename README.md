# Automatic File Organizer 📁

A Python tool that automatically organizes files into folders based on their file extensions.

## Features

- Automatically sorts files into categories.
- Supports images, documents, audio, videos, and archives.
- Creates category folders automatically.
- Prevents duplicate filenames from being overwritten.
- Preview mode to see changes before moving files.
- Command-line options for custom folders.
- Logs successful file moves in `organizer.log`.
- Validates folder paths and handles errors.

## File Categories

| Category | Extensions |
|---|---|
| Images | .jpg, .jpeg, .png, .gif |
| Documents | .pdf, .docx, .txt, .doc |
| Audio | .mp3, .wav, .flac |
| Videos | .mp4, .mov, .avi |
| Archives | .zip, .rar, .7z |
| Others | All other extensions |

## Requirements

- Python 3.8 or newer
- No external Python packages required.

## Installation

Clone the repository:

```bash
git clone https://github.com/XereX056/automatic-file-organizer.git
```

Navigate into the project:

```bash
cd automatic-file-organizer
```

## Usage

### Preview mode (default)

Preview the changes without moving files:

```bash
python main.py
```

### Organize files

Move files into their category folders:

```bash
python main.py --move
```

### Choose a custom folder

Preview files in a different folder:

```bash
python main.py another_test
```

Actually organize that folder:

```bash
python main.py --move another_test
```

## Logging

Successful file moves are recorded in `organizer.log`, including timestamps.

## Project Structure

```text
automatic-file-organizer/
├── main.py
├── .gitignore
├── README.md
└── organizer.log
```

## Author

[XereX056](https://github.com/XereX056)