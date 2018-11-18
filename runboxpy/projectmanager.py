from pathlib import Path
# import os


class Project:
    def __init__(self, generate_location: str, name: str):
        self.generate_location = Path(generate_location)
        self.name = name

    def generate_project(self):
        self.make_placing_dir()
        self.make_project_dir()

    def make_placing_dir(self):
        self.generate_location.mkdir()

    def make_project_dir(self):
        files_dir = self.generate_location / self.name
        files_dir.mkdir()

        # if not os.path.exists(dir_location):
        # if not os.path.exists(files_dir):
