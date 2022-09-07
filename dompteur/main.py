import os
import pathlib
import shutil
import subprocess
import sys

import tomli
from platformdirs import user_config_path

from dompteur.ui import DompteurApp, CreatorApp, ImporterApp
from dompteur.stores import ProjectsStore

TEMPLATE_DIR = pathlib.Path(f'{os.path.dirname(__file__)}/templates')
DOMPTEUR_TEMPLATE = TEMPLATE_DIR / "dompteur.toml.template"

CONF_DIR = user_config_path('dompteur')
DOMP_CONF = CONF_DIR / "dompteur.toml"

class SimpleStart(DompteurApp):
    def __init__(self):
        super().__init__()

        self._read_configs()
        conf_button = self.builder.get_object('conf_dir_button')
        conf_button.config(text = str(CONF_DIR))

    def _read_configs(self) -> None:
        """
        Care about the config files, create them if they do not exist otherwise read them
        via a toml-parser.
        :return: None
        """
        os.makedirs(CONF_DIR, exist_ok=True)

        # Dompteur Config
        if not os.path.exists(DOMP_CONF):
            shutil.copy(DOMPTEUR_TEMPLATE, DOMP_CONF)

        with open(DOMP_CONF, "rb") as f:
            config = tomli.load(f)

        # Projects folder
        projects_folder = config['paths']['projects_folder']
        if os.path.isabs(projects_folder):
            self.projects_folder = projects_folder
        else:
            self.projects_folder = CONF_DIR / projects_folder
        os.makedirs(self.projects_folder, exist_ok=True)

        # Template folders
        templates_folder = config['paths']['templates_folder']
        if os.path.isabs(templates_folder):
            self.templates_folder = templates_folder
        else:
            self.templates_folder = CONF_DIR / templates_folder
        os.makedirs(self.templates_folder, exist_ok=True)

    def open_create(self):
        CreatorApp()

    def open_import(self):
        ImporterApp()
        ProjectsStore(self.projects_folder)

    def open_conf(self):
        if sys.platform == 'darwin':
            subprocess.check_call(['open', str(CONF_DIR)])
        elif sys.platform == 'linux':
            subprocess.check_call(['xdg-open', str(CONF_DIR)])
        elif sys.platform == 'win32':
            subprocess.check_call(['explorer', str(CONF_DIR)])

    def raise_frame(self, *args):
        pass

if __name__ == "__main__":
    app = SimpleStart()
    app.run()
