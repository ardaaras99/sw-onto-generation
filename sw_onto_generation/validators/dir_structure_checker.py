# %%
from pathlib import Path

from rich import print as rprint

from sw_onto_generation import ENUM_CLASSES


class DIRManager:
    def __init__(self, root_path: Path):
        self.root_path = root_path

    def create_from_structure(self, structure: dict[str, list[str]]):
        for lib_name, onto_names in structure.items():
            lib_path = self.root_path / f"lib_{lib_name}"
            lib_path.mkdir(exist_ok=True, parents=True)
            for onto_name in onto_names:
                onto_path = lib_path / f"onto_{onto_name}"
                onto_path.mkdir(exist_ok=True, parents=True)
                (onto_path / "nodes.py").touch()
                (onto_path / "relations.py").touch()

    def check_validity(self):
        issues = []

        # Check if root directory exists
        if not self.root_path.exists():
            issues.append(f"Root directory '{self.root_path}' does not exist")
            return issues

        # Level 1: Check root directory contents
        valid_lib_names = [f"lib_{enum_class.__name__}" for enum_class in ENUM_CLASSES]
        root_items = list(self.root_path.iterdir())

        # Check for unexpected items in root directory
        for item in root_items:
            if item.name not in valid_lib_names:
                issues.append(f"Unexpected item '{item}' in root directory")

        if issues:
            rprint("[bold red]Directory structure issues found:[/bold red]")
            for issue in issues:
                rprint(f"- {issue}")
            return issues

        # Level 2: Check library directories
        for enum_class in ENUM_CLASSES:
            lib_name = enum_class.__name__
            lib_path = self.root_path / f"lib_{lib_name}"

            # Skip if library directory doesn't exist
            if not lib_path.exists():
                issues.append(f"Expected library directory '{lib_path}' does not exist")
                continue

            # Get valid ontology names for this enum class
            valid_onto_names = [f"onto_{e.value}" for e in enum_class]
            lib_items = list(lib_path.iterdir())

            # Check for unexpected items in library directory
            for item in lib_items:
                if item.name not in valid_onto_names:
                    issues.append(f"Unexpected item '{item}' in library directory '{lib_path}'")

        if issues:
            rprint("[bold red]Validation issues found:[/bold red]")
            for issue in issues:
                rprint(f"- {issue}")
            return issues

        # Level 3: Check ontology directories
        for enum_class in ENUM_CLASSES:
            lib_name = enum_class.__name__
            lib_path = self.root_path / f"lib_{lib_name}"

            for onto_enum in enum_class:
                onto_name = onto_enum.value
                onto_path = lib_path / f"onto_{onto_name}"

                # Skip if ontology directory doesn't exist
                if not onto_path.exists():
                    issues.append(f"Expected ontology directory '{onto_path}' does not exist")
                    continue

                # Check files in ontology directory
                required_files = ["nodes.py", "relations.py"]
                onto_items = list(onto_path.iterdir())

                # Check for missing required files
                for file_name in required_files:
                    file_path = onto_path / file_name
                    if not file_path.exists():
                        issues.append(f"Required file '{file_path}' does not exist")

                # Check for unexpected items in ontology directory
                for item in onto_items:
                    if item.name not in required_files:
                        issues.append(f"Unexpected item '{item}' in ontology directory '{onto_path}'")

        if issues:
            rprint("[bold red]Validation issues found:[/bold red]")
            for issue in issues:
                rprint(f"- {issue}")
        else:
            rprint("[bold green]Directory structure is valid![/bold green]")

        return issues


# %%

# %%
