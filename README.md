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
1. Clone the repo:
