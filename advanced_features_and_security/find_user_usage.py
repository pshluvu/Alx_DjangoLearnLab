import os

# Set the root directory to your project
project_root = os.path.abspath(".")  # assumes you're running from project root

# The keyword we're searching for
keyword = "User"

# Walk through all files
for dirpath, dirnames, filenames in os.walk(project_root):
    for filename in filenames:
        if filename.endswith(".py"):
            filepath = os.path.join(dirpath, filename)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    for i, line in enumerate(f, 1):
                        if keyword in line:
                            print(f"{filepath}:{i}: {line.strip()}")
            except Exception as e:
                print(f"Could not read {filepath}: {e}")
