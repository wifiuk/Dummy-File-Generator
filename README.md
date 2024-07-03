**Overview**

The Dummy File Generator Script is designed to create a variety of dummy files for testing purposes. It generates files of different types with realistic content, including text, CSV, JSON, XML, HTML, log, markdown, JPEG, PDF, and ZIP files. This script can be customized to generate a specified number of files, with adjustable content characteristics and distribution.

**Features**
- Generates Multiple File Types: txt, csv, json, xml, html, log, md, jpg, pdf, and zip.
- Customizable Content: Control the amount of content in each file type.
- Random File Names: Files are named using random English words.
- Random Creation Dates: File creation dates are spread over the past year.
- Parallel Processing: Utilizes multiprocessing to generate files efficiently.
- Optional Logging: Enable or disable logging as needed.

**Dependencies**

Ensure you have the following dependencies installed:

- Pillow (for handling JPEG images)
- FPDF (for creating PDF files)
- lorem (for generating random English sentences)

To install the required dependencies, run:
```
pip install pillow fpdf lorem
```

**Usage Instructions**

Download the Script:

Save the script as generate_dummy_files.py.

**Customize Options:**

Open the script in a text editor.
Customize the options at the top of the script as needed:
```
# --- Customization Options ---
NUM_FILES = 300  # Number of files to generate
OUTPUT_DIR = "dummy_files"  # Directory to save the generated files
ZIP_PERCENTAGE = 0.05  # Percentage of total files that should be ZIP files
MIN_SENTENCES = 1  # Minimum number of sentences in text-based content
MAX_SENTENCES = 5  # Maximum number of sentences in text-based content
MIN_ROWS = 5  # Minimum number of rows in CSV files
MAX_ROWS = 20  # Maximum number of rows in CSV files
MIN_COLS = 2  # Minimum number of columns in CSV files
MAX_COLS = 10  # Maximum number of columns in CSV files
MIN_WIDTH = 50  # Minimum width of JPEG images
MAX_WIDTH = 500  # Maximum width of JPEG images
MIN_HEIGHT = 50  # Minimum height of JPEG images
MAX_HEIGHT = 500  # Maximum height of JPEG images
ENABLE_LOGGING = False  # Set to True to enable logging
# -----------------------------
```

**Run the Script:**

Execute the script using Python 3:
```
python3 generate_dummy_files.py
```
**Check Output:**

The generated files will be saved in the specified output directory (dummy_files by default).
If logging is enabled (ENABLE_LOGGING = True), logs will provide detailed information about the process.

**Customization Options**

- NUM_FILES: Total number of files to generate.
- OUTPUT_DIR: Directory where the generated files will be saved.
- ZIP_PERCENTAGE: Percentage of total files that should be ZIP files.
- MIN_SENTENCES, MAX_SENTENCES: Range for the number of sentences in text-based files (e.g., txt, md).
- MIN_ROWS, MAX_ROWS: Range for the number of rows in CSV files.
- MIN_COLS, MAX_COLS: Range for the number of columns in CSV files.
- MIN_WIDTH, MAX_WIDTH: Range for the width of JPEG images.
- MIN_HEIGHT, MAX_HEIGHT: Range for the height of JPEG images.
- ENABLE_LOGGING: Enable or disable logging. Set to True to enable logging, False to disable.

**Example Use Case**

Scenario: Running a Breach and Attack Simulation (BAS) Ransomware Simulation

When conducting a BAS ransomware simulation, you need a set of files to encrypt in order to test the effectiveness of your ransomware detection and response systems. Using real-world company files poses a risk of accidental data leaks or corruption. Instead, you can use this script to generate a large set of dummy files that mimic real files in structure and content without containing any sensitive information.

**Steps:**

Configure the Script:

Set the number of files, output directory, and other parameters according to your simulation requirements.
Example customization:
```
# --- Customization Options ---
NUM_FILES = 500
OUTPUT_DIR = "simulation_files"
ZIP_PERCENTAGE = 0.10
MIN_SENTENCES = 2
MAX_SENTENCES = 10
MIN_ROWS = 10
MAX_ROWS = 30
MIN_COLS = 3
MAX_COLS = 15
MIN_WIDTH = 100
MAX_WIDTH = 600
MIN_HEIGHT = 100
MAX_HEIGHT = 600
ENABLE_LOGGING = True
# -----------------------------
```

Generate Dummy Files:

Run the script to generate the files:
```
python3 generate_dummy_files.py
```

Use Generated Files in Simulation:

Use the generated files in the simulation_files directory as the target for your ransomware simulation.
Monitor and analyze how your detection and response systems handle the encryption of these files.
By using dummy files, you can safely conduct comprehensive ransomware simulations without risking real data, ensuring your security systems are robust and effective.
