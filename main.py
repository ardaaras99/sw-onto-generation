# %%

import importlib
import os
import sys
from pathlib import Path


def find_python_files(directory: str = ".") -> list[Path]:
    """Find all .py files in the given directory and its subdirectories."""
    python_files = []
    # Get the absolute path of the directory
    # Get the project root director

    for root, _, files in os.walk(directory):
        # Skip the venv directory, git directory, and other non-source directories
        if any(skip_dir in root for skip_dir in [".venv", ".git", "__pycache__", ".mypy_cache", ".ruff_cache"]):
            continue

        for file in files:
            if file.endswith(".py"):
                python_files.append(Path(os.path.join(root, file)))

    return python_files


def convert_path_to_module(file_path: Path) -> str:
    """Convert a file path to a module path that can be imported."""
    # Get the relative path as a string
    rel_path = str(file_path)

    # Remove ./ prefix if it exists
    if rel_path.startswith("./"):
        rel_path = rel_path[2:]

    # Remove .py extension and replace / with .
    module_path = rel_path.replace("/", ".").replace("\\", ".")[:-3]

    return module_path


def test_imports() -> list[tuple[str, bool, str]]:
    """Test importing all Python files in the project.

    Returns:
        List of tuples containing (module_name, success, error_message)
    """
    results = []
    python_files = find_python_files()

    for file_path in python_files:
        # Skip test files and this script itself
        if "test_" in str(file_path) or file_path.name == "main.py":
            continue

        try:
            module_path = convert_path_to_module(file_path)
            # Try to import the module
            importlib.import_module(module_path)
            results.append((str(file_path), True, ""))
        except Exception as e:
            results.append((str(file_path), False, str(e)))

    return results


def main():
    """Run the import tests and print the results."""
    print("Testing if all Python files can be imported...")

    results = test_imports()

    # Print the results
    success_count = 0
    fail_count = 0

    for file_path, success, error in results:
        if success:
            print(f"✅ {file_path}")
            success_count += 1
        else:
            print(f"❌ {file_path}: {error}")
            fail_count += 1

    # Print summary
    total = success_count + fail_count
    print(f"\nSummary: {success_count}/{total} files imported successfully")
    print(f"         {fail_count}/{total} files failed to import")

    # Return non-zero exit code if any imports failed
    return 0 if fail_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())

# %%
