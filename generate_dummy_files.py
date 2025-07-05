import os
import random
import lorem
from datetime import datetime, timedelta
from PIL import Image
from fpdf import FPDF
import zipfile
import io
import csv
import json
import xml.etree.ElementTree as ET
from multiprocessing import Pool
import logging

# --- Customization Options ---
NUM_FILES = 300
OUTPUT_DIR = "dummy_files"
ZIP_PERCENTAGE = 0.05
MIN_SENTENCES = 1
MAX_SENTENCES = 5
MIN_ROWS = 5
MAX_ROWS = 20
MIN_COLS = 2
MAX_COLS = 10
MIN_WIDTH = 50
MAX_WIDTH = 500
MIN_HEIGHT = 50
MAX_HEIGHT = 500
ENABLE_LOGGING = False  # Set to True to enable logging
# -----------------------------

if ENABLE_LOGGING:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Fixed list of supported file types
FILE_TYPES = ['txt', 'csv', 'json', 'xml', 'html', 'log', 'md', 'jpg', 'pdf']

# Predefined list of common English words
COMMON_ENGLISH_WORDS = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon",
    "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "ugli", "vine",
    "watermelon", "xigua", "yellow", "zucchini", "avocado", "blueberry", "coconut", "dragonfruit", "eggplant"
]

def generate_random_english_text(min_sentences=MIN_SENTENCES, max_sentences=MAX_SENTENCES):
    """Generate random English sentences."""
    return ' '.join(lorem.sentence() for _ in range(random.randint(min_sentences, max_sentences)))

def generate_random_english_word():
    """Generate a random English word."""
    return random.choice(COMMON_ENGLISH_WORDS)

def create_dummy_jpeg(file_path):
    """Create a dummy JPEG image."""
    width, height = random.randint(MIN_WIDTH, MAX_WIDTH), random.randint(MIN_HEIGHT, MAX_HEIGHT)
    img = Image.new('RGB', (width, height), color=(73, 109, 137))
    img.save(file_path)

def create_dummy_pdf(file_path):
    """Create a dummy PDF with valid English text."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for _ in range(random.randint(1, 5)):
        pdf.multi_cell(0, 10, generate_random_english_text())
    pdf.output(file_path)

def create_dummy_zip(file_path, included_files):
    """Create a dummy ZIP file containing a mix of other file types."""
    with zipfile.ZipFile(file_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file in included_files:
            zf.write(file, os.path.basename(file))

def create_dummy_csv(file_path):
    """Create a dummy CSV file with random headers and cells."""
    num_rows = random.randint(MIN_ROWS, MAX_ROWS)
    num_cols = random.randint(MIN_COLS, MAX_COLS)
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([f'Header{i+1}' for i in range(num_cols)])
        for _ in range(num_rows):
            writer.writerow([generate_random_english_text(1, 3) if random.choice([True, False]) else random.randint(1, 100) for _ in range(num_cols)])

def create_dummy_json(file_path):
    """Create a dummy JSON file with random key-value pairs."""
    data = {f'key{i}': generate_random_english_text(1, 3) for i in range(random.randint(5, 15))}
    with open(file_path, 'w') as file:
        json.dump(data, file)

def create_dummy_xml(file_path):
    """Create a dummy XML file with random elements."""
    root = ET.Element('root')
    for i in range(random.randint(5, 15)):
        item = ET.SubElement(root, 'item', attrib={'id': str(i)})
        item.text = generate_random_english_text(1, 3)
    tree = ET.ElementTree(root)
    tree.write(file_path)

def create_dummy_html(file_path):
    """Create a dummy HTML file with random content."""
    html_content = f"""
    <html>
        <head><title>Dummy HTML</title></head>
        <body>
            <h1>{generate_random_english_text(1, 2)}</h1>
            <p>{generate_random_english_text()}</p>
        </body>
    </html>
    """
    with open(file_path, 'w') as file:
        file.write(html_content)

def create_dummy_log(file_path):
    """Create a dummy log file with random log entries."""
    num_lines = random.randint(10, 50)
    with open(file_path, 'w') as file:
        for _ in range(num_lines):
            file.write(f'{datetime.now()}: {generate_random_english_text(1, 3)}\n')

def create_file(file_type, file_path):
    """Create a file based on the specified type."""
    creation_functions = {
        'jpg': create_dummy_jpeg,
        'pdf': create_dummy_pdf,
        'csv': create_dummy_csv,
        'json': create_dummy_json,
        'xml': create_dummy_xml,
        'html': create_dummy_html,
        'log': create_dummy_log,
        'md': lambda path: open(path, 'w').write(f"# {generate_random_english_text(1, 2)}\n\n{generate_random_english_text()}"),
        'txt': lambda path: open(path, 'w').write(generate_random_english_text())
    }
    
    if file_type in creation_functions:
        creation_functions[file_type](file_path)
    else:
        if ENABLE_LOGGING:
            logging.error(f"No function to handle file type: {file_type}")

def create_dummy_file(file_idx, output_dir, one_year_ago):
    """Create a single dummy file."""
    file_date = one_year_ago + timedelta(days=random.randint(0, 365))
    file_type = random.choice(FILE_TYPES)
    file_name = f"{generate_random_english_word()}_{file_idx}.{file_type}"
    file_path = os.path.join(output_dir, file_name)

    try:
        create_file(file_type, file_path)
        os.utime(file_path, (file_date.timestamp(), file_date.timestamp()))
        return file_path
    except Exception as e:
        if ENABLE_LOGGING:
            logging.error(f"Error creating file {file_path}: {e}")
        return None

def create_dummy_files(num_files=NUM_FILES, output_dir=OUTPUT_DIR):
    """Create multiple dummy files with specified configurations."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    one_year_ago = datetime.now() - timedelta(days=365)
    all_files = []

    with Pool() as pool:
        results = [pool.apply_async(create_dummy_file, (i, output_dir, one_year_ago)) for i in range(num_files)]
        all_files = [res.get() for res in results if res.get() is not None]

    num_zip_files = int(num_files * ZIP_PERCENTAGE)
    for i in range(num_zip_files):
        zip_name = f"{generate_random_english_word()}_zip_{i}.zip"
        zip_path = os.path.join(output_dir, zip_name)
        included_files = random.sample(all_files, random.randint(1, 10))
        create_dummy_zip(zip_path, included_files)
        all_files.append(zip_path)
        file_date = one_year_ago + timedelta(days=random.randint(0, 365))
        os.utime(zip_path, (file_date.timestamp(), file_date.timestamp()))

    if ENABLE_LOGGING:
        logging.info(f"{num_files} dummy files created in '{output_dir}' directory.")

if __name__ == "__main__":
    create_dummy_files()
