from pathlib import Path
import unittest

from tsukushi.projectmanager import ProjectMaker


class MockMkdir:
    pass


class TestProjectMaker(unittest.TestCase):
    def setUp(self):
        self.orig_mkdir = Path.mkdir
        Path.mkdir = MockMkdir

    def test_generate_project(self):
        project_maker = ProjectMaker("~/Projects")
        project = project_maker.generate_project("test_project")
        self.assertEqual(str(project.files_location),
                         "~/Projects/test_project")
        self.assertEqual(project.name, "test_project")


if __name__ == "__main__":
    unittest.main()
