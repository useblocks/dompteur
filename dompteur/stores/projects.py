import os
import sys
import threading
import subprocess

import tomli

class ProjectsStore:
    """
    Store data about Sphinx projects and allow to import existing project or remove them.

    """

    def __init__(self, projects_folder):
        self.projects_folder = projects_folder
        self.projects = {}
        self.status = {}

        self.load_projects()

    def load_projects(self):
        for file in [f for f in os.listdir(self.projects_folder) if f.endswith('.toml')]:
            file_path = self.projects_folder / file

            with open(file_path, "rb") as f:
                proj_conf = tomli.load(f)
                self.projects[proj_conf['name']] = proj_conf

    def import_project(self):
        pass

    def remove_project(self):
        pass

    def build_project(self, project, builder):
        project_conf = self.projects[project]
        build_conf = project_conf['builds'][builder.lower()]
        if build_conf.get('own_command', False):
            args = build_conf['own_command'].split(' ')
        else:
            args = [
                'sphinx-build',
                '-b',
                build_conf['builder'],
                build_conf['source_dir'],
                build_conf['build_dir'],
            ]
        cwd = project_conf['working_dir']
        process = subprocess.Popen(args, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return process
