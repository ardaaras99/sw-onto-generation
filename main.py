# %%
from pathlib import Path

from sw_onto_generation import DIR_STRUCTURE
from sw_onto_generation.validators.compile_checker import test_imports
from sw_onto_generation.validators.dir_structure_checker import DIRManager


def main() -> None:
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
    dir_manager = DIRManager(root_path=Path("sw_onto_generation/root"))
    dir_manager.create_from_structure(DIR_STRUCTURE)
    dir_manager.check_validity()


if __name__ == "__main__":
    main()

# %%
