import contextlib
import io
import os
from pathlib import Path
import shutil
import subprocess
import sys
from tkinter import ttk, DISABLED, NORMAL, END
import threading

import tomli
from platformdirs import user_config_path

from dompteur.ui import DompteurApp, CreatorApp, ImporterApp
from dompteur.stores import ProjectsStore

TEMPLATE_DIR = Path(f'{os.path.dirname(__file__)}/templates')
DOMPTEUR_TEMPLATE = TEMPLATE_DIR / "dompteur.toml.template"

CONF_DIR = user_config_path('dompteur')
DOMP_CONF = CONF_DIR / "dompteur.toml"


class SimpleStart(DompteurApp):
    def __init__(self):
        super().__init__()

        self.build_combos = {}

        self._read_configs()
        conf_button = self.builder.get_object('conf_dir_button')
        conf_button.config(text=str(CONF_DIR))

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
            self.config = tomli.load(f)

        # Projects folder
        projects_folder = self.config['paths']['projects_folder']
        if os.path.isabs(projects_folder):
            self.projects_folder = projects_folder
        else:
            self.projects_folder = CONF_DIR / projects_folder
        os.makedirs(self.projects_folder, exist_ok=True)

        # Template folders
        templates_folder = self.config['paths']['templates_folder']
        if os.path.isabs(templates_folder):
            self.templates_folder = templates_folder
        else:
            self.templates_folder = CONF_DIR / templates_folder
        os.makedirs(self.templates_folder, exist_ok=True)

        self.prj_store = ProjectsStore(self.projects_folder)
        self._update_projects_gui()

    def _update_projects_gui(self):
        index = 0
        projects_frame = self.builder.get_object('projects_frame')

        for name, project in self.prj_store.projects.items():

            # Add line 
            if index > 0:
                line_frame = ttk.Frame(projects_frame)
                line_frame.configure(height=2, style="Sphinx_M.TFrame", width=700)
                line_frame.pack(expand="true", fill="y", pady=10, side="top")
            index += 1

            self._create_project_row(projects_frame, name)

    def _create_project_row(self, projects_frame, name):
        project = self.prj_store.projects[name]

        project_frame = ttk.Frame(projects_frame)
        project_frame.configure(height=2, style="Sphinx_R.TFrame")

        project_label = ttk.Label(project_frame)
        project_label.configure(
            anchor="n",
            justify="right",
            style="Sphinx_R.TLabel",
            text=name,
            width=20,
        )
        project_label.grid(column=0, ipadx=0, row=0)

        builders_combo_name = f'builders_combo_{name}'

        build_button = ttk.Button(project_frame)

        builders_combo = ttk.Combobox(project_frame, name=builders_combo_name)
        builders_combo.configure(
            exportselection="true",
            validate="focusin",
            values=" ".join([x.upper() for x in project['builds'].keys()]),
            width=15
        )
        builders_combo.current(0)

        build_button.configure(style="Sphinx_R.TButton",
                               text=f"⚒ Build",
                               command=lambda: self.build_docs(name, builders_combo, build_button))

        build_button.grid(column=2, padx=2, row=0)

        builders_combo.grid(column=1, padx=0, row=0)

        show_button = ttk.Button(project_frame)
        show_button.configure(
            cursor="arrow",
            style="Sphinx_R.TButton",
            text="👁 Show",
            command=lambda: self.show_docs(name, builders_combo)
        )
        show_button.grid(column=4, padx=2, row=0)
        edit_button = ttk.Button(project_frame)
        edit_button.configure(
            cursor="arrow", style="Sphinx_R.TButton", text="🖋 Edit",
            command=lambda: self.edit_docs(name, builders_combo)
        )
        edit_button.grid(column=5, padx=2, row=0)
        conf_button = ttk.Button(project_frame)
        conf_button.configure(style="Sphinx_R.TButton", text="⚙ Configure")
        conf_button.grid(column=6, padx=20, row=0)
        project_frame.pack(side="top")
        project_frame.grid_anchor("center")

    def open_create(self):
        CreatorApp()

    def open_import(self):
        ImporterApp()

    def build_docs(self, name, builders_combo, build_button):
        self.builder.get_object('console').delete("1.0", END)
        builder = builders_combo.get()
        org_text = build_button.cget('text')
        build_button.configure(state=DISABLED, text="Building...")
        build_button.update()  # Needed to show new text immediately
        process = self.prj_store.build_project(name, builder)
        os.set_blocking(process.stdout.fileno(), False)
        os.set_blocking(process.stderr.fileno(), False)
        self._monitor(process, build_button, org_text)

    def _monitor(self, process, build_button, org_text):
        console = self.builder.get_object('console')

        if process.poll() is None:
            lines = process.stdout.readlines()
            lines_error = process.stderr.readlines()
            console.insert("end-1c", "".join([x.decode("utf-8")for x in lines]))
            console.insert("end-1c", "".join([x.decode("utf-8")for x in lines_error]))
            console.see(END)
            self.builder.get_object('main').after(50, lambda: self._monitor(process, build_button, org_text))
        else:
            build_button.update()  # Need to disable clicks for DISABLED buttons
            build_button.configure(state=NORMAL, text=org_text)

    def show_docs(self, name, builders_combo):
        builder = builders_combo.get()
        project_conf = self.prj_store.projects[name]
        build_conf = project_conf['builds'][builder.lower()]

        build_path = Path(project_conf['working_dir']) / build_conf['build_dir']

        build_show = build_conf.get('show_command', False)
        if build_show:
            args = build_show.split(' ')
            subprocess.run(args, cwd=project_conf['working_dir'])
        else:
            self._os_open(build_path)

    def edit_docs(self, name, builder_combo):
        ide_command = self.config.get('ide_command', False)
        if not ide_command:
            return

        prj_conf = self.prj_store.projects[name]
        prj_cwd = prj_conf.get('working_dir')

        if not prj_cwd:
            return

        args = [ide_command, prj_cwd]

        subprocess.run(args)



    def open_conf(self):
        self._os_open(CONF_DIR)

    def _os_open(self, path):
        if sys.platform == 'darwin':
            subprocess.check_call(['open', str(path)])
        elif sys.platform == 'linux':
            subprocess.check_call(['xdg-open', str(path)])
        elif sys.platform == 'win32':
            subprocess.check_call(['explorer', str(path)])


if __name__ == "__main__":
    app = SimpleStart()
    app.run()
