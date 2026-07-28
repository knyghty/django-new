import io
import os
import pathlib
import tempfile
from unittest import mock

from django.core.management import call_command
from django.test import SimpleTestCase


class NewCommandTests(SimpleTestCase):
    def create_project(self, choice, project_name):
        old_cwd = os.getcwd()
        with tempfile.TemporaryDirectory() as tmp:
            os.chdir(tmp)
            try:
                with mock.patch("builtins.input", return_value=choice):
                    call_command("new", project_name, stdout=io.StringIO())
                return {
                    str(path.relative_to(tmp))
                    for path in pathlib.Path(tmp).rglob("*")
                    if path.is_file()
                }
            finally:
                os.chdir(old_cwd)

    def test_default_project(self):
        files = self.create_project("1", "myproject")
        self.assertIn("myproject/manage.py", files)
        self.assertIn("myproject/myproject/settings.py", files)

    def test_single_file_project(self):
        files = self.create_project("2", "myproject")
        self.assertIn("myproject/main.py", files)

    def test_classic_project(self):
        files = self.create_project("3", "myproject")
        self.assertIn("myproject/manage.py", files)
        self.assertIn("myproject/myproject/settings.py", files)
