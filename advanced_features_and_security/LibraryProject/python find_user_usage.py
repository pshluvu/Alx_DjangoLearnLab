import os
import re

# Root directory of your project
PROJECT_ROOT = os.path.join(os.getcwd())

# Regex patterns
user_import_pattern = re.compile(r"from\s+django\.contrib\.auth\.models\s+import\s+settings.AUTH_USER_MODEL")
user_field_pattern = re.compile(r"\bUser\b")

def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    modified = False

    # Replace settings.AUTH_USER_MODEL import
    if user_import_pattern.search(content):
        content = user_import_pattern.sub("from django.conf import settings", content)
        modified = True

    # Replace settings.AUTH_USER_MODEL field references
    if user_field_pattern.search(content):
        content = user_field_pattern.sub("settings.AUTH_USER_MODEL", content)
        modified = True

    if modified:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated: {file_path}")

def scan_project(root_dir):
    for subdir, _, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(subdir, file)
                process_file(file_path)

if __name__ == "__main__":
    scan_project(PROJECT_ROOT)
    print("All Python files processed.")
