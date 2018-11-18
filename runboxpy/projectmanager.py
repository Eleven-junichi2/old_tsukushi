from pathlib import Path
# import os


class Project:
    def __init__(self, files_location: str):
        self.files_location = Path(files_location)
        self.name = self.files_location.parts[-1]


class ProjectMaker:
    def __init__(self, generate_location: str):
        self.generate_location = Path(generate_location)

    def generate_project(self, name):
        self.make_placing_dir()
        self.make_project_dir(name)
        self.files_location = self.generate_location / name
        return Project(self.files_location)

    def make_placing_dir(self):
        self.generate_location.mkdir()

    def make_project_dir(self, name):
        self.files_location = self.generate_location / name
        self.files_location.mkdir()
