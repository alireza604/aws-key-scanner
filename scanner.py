import re
import sys
import os

# Regex pattern for AWS Access Key ID (starts with AKIA, ASIA, etc., followed by 16 uppercase letters/numbers)
AWS_KEY_PATTERN = r'(A3T[A-Z0-9]|AKIA|ASIA|ABIA|ACCA)[A-Z0-9]{16}'

def scan_file(file_path):
    """Scan a single file for AWS keys."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            matches = re.findall(AWS_KEY_PATTERN, content)
            if matches:
                print(f"Potential AWS keys found in {file_path}:")
                for match in matches:
                    print(f" - {match}")
            else:
                print(f"No AWS keys found in {file_path}.")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

def scan_directory(directory):
    """Scan all text files in a directory."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.txt', '.py', '.js', '.json', '.md')):  # Add more extensions as needed
                scan_file(os.path.join(root, file))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scanner.py <file_or_directory>")
        sys.exit(1)
    
    path = sys.argv[1]
    if os.path.isfile(path):
        scan_file(path)
    elif os.path.isdir(path):
        scan_directory(path)
    else:
        print("Invalid path provided.")
