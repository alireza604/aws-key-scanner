# AWS Key Scanner

A simple Python tool for bug bounty hunters to scan text files or directories for potential AWS access keys. This helps identify credential leaks during reconnaissance or code audits.

**Disclaimer**: This is for educational and ethical use only. Always obtain permission before scanning any systems or data.

## Features
- Regex-based detection of AWS Access Key IDs.
- Scan single files or entire directories.
- Supports common file types like .txt, .py, .js, etc.

## Requirements
- Python 3.x
- No external libraries needed (uses built-in `re` and `os`).

## Installation
1. Clone the repo: git clone https://github.com/alireza604/aws-key-scanner.git
2. Navigate to the directory: cd aws-key-scanner

   
## Usage
Run the script from the command line:

- Scan a single file: python scanner.py path/to/file.txt

- Scan a directory: python scanner.py path/to/directory

Example output: 
Potential AWS keys found in example.txt:AKIAIOSFODNN7EXAMPLE
OR
No AWS keys found in clean_file.py.


## How It Works
The script uses a regex pattern `(A3T[A-Z0-9]|AKIA|ASIA|ABIA|ACCA)[A-Z0-9]{16}` to match common AWS key formats. It reads files line-by-line and reports matches.

## Contributing
Feel free to fork and submit pull requests! Ideas: Add support for AWS Secret Access Keys, integrate with GitHub API, or add logging.










