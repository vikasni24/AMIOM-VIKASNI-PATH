import os
import shutil

class FileManager:
    @staticmethod
    def read_file(filepath: str) -> str:
        """Reads the content of the given file."""
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()

    @staticmethod
    def write_file(filepath: str, content: str):
        """Writes content to the given file, overwriting it."""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

    @staticmethod
    def create_backup(filepath: str) -> str:
        """Creates a backup of the original file."""
        backup_path = f"{filepath}.bak"
        shutil.copy2(filepath, backup_path)
        return backup_path
