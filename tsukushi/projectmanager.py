from pathlib import Path
# import os


class Project:
    def __init__(self, files_location: str):
        self.files_location = Path(files_location)
        self.name = self.files_location.parts[-1]


class ProjectMaker:
    def __init__(self, generate_location: str):
        """
        Args:
            generate_location (str): for where make project directory.
        """
        self.generate_location = Path(generate_location)

    def generate_project(self, name):
        print("genepro")
        self.make_placing_dir()
        self.make_project_dir(name)
        files_location = self.generate_location / name
        return Project(files_location)

    def make_placing_dir(self):
        print("genepro mplace")
        self.generate_location.mkdir(exist_ok=True)

    def make_project_dir(self, name):
        print("genepro  mpd")
        files_location = Path(self.generate_location) / name
        files_location.mkdir(exist_ok=True)
