from django.core.management import BaseCommand
from django.core.management import call_command

from ...conf import TEMPLATES_DIR


PROJECT_STRUCTURE_MAP = {
    "1": f"{TEMPLATES_DIR}/default",
    "2": f"{TEMPLATES_DIR}/single_file",
    "3": f"{TEMPLATES_DIR}/classic",
}


class Command(BaseCommand):
    help = "Create a new Django project."

    def add_arguments(self, parser):
        parser.add_argument("project_name", type=str)

    def handle(self, *args, **options):
        project_name = options["project_name"]
        self.stdout.write("Which type of project would you like to create?")
        self.stdout.write("1: Quick start Django project")
        self.stdout.write("2: Single file project")
        self.stdout.write("3: A classic project")
        self.stdout.write("You may also enter a path or URL to a custom template")
        project_structure = input()
        project_template = PROJECT_STRUCTURE_MAP.get(project_structure, project_structure)
        call_command("startproject", project_name, template=project_template)
