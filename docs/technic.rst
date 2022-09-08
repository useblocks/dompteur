Technic
=======

Stack
-----

Dompteur is based on:

* Tkinter and pygubu as GUI-Designer


Workflow
--------

Tool init
~~~~~~~~~

.. uml::
   :width: 99%

   @startuml
   title Tool Init

   actor User as user
   participant App as app #ee4444
   participant GUI as gui #ee4444
   control "project_store" as ps #ee4444
   control "template_store" as ts #ee4444
   collections app_config as ac #ee4444
   collections proj_configs as pc #ee4444
   collections template_configs as tc #ee4444

   user --> app : start dompteur
   app <--> ac: load app config
   app <--> ps : init Project store
   ps <--> pc: load project configs
   app <--> ts : init Template store
   ts <--> tc: load template configs
   app --> gui: init GUI
   gui --> ps: Request projects
   ps --> gui: Provide projects

   loop Show projects
   gui --> gui: Show project row
   gui --> gui: Fill "builder" selector
   end

   @enduml

Project import
~~~~~~~~~~~~~~
Add an existing project to dompteur.


.. uml::
   :width: 99%

   @startuml
   title Project import and config

   actor User as user
   participant App as app #ee4444
   participant GUI as gui #ee4444
   control "project_store" as ps #ee4444
   collections proj_configs as pc #ee4444

   user --> gui: presses "Import project"
   gui --> gui: Shows import screen
   user --> gui: Selects project conf.py
   gui --> ps: triggers "project_import()"
   ps --> ps: Imports project and data
   ps --> pc: Create project config file
   gui --> gui: Shows "Project config screen"
   user --> gui: configures project
   gui --> ps: triggers "project_update()"
   ps --> pc: Updates config file
   gui --> gui: Returns to overview screen



   @enduml



Build selection and start
~~~~~~~~~~~~~~~~~~~~~~~~~

.. uml::
   :width: 99%

   @startuml
   title Build start

   actor User as user
   participant App as app #ee4444
   participant GUI as gui #ee4444
   control "project_store" as ps #ee4444
   participant Sphinx as sphinx #3388dd

   user --> gui : presses "build" button
   gui --> ps: Executes "project_build()"
   ps --> sphinx: starts "sphinx-build"
   group during sphinx-build
      sphinx --> sphinx: build docs
      ps <--> sphinx: fetches and stores stdout/stderr
      ps <--> ps: stores running time\n and build progress
      gui <--> : Reads build status data
      gui --> gui: Update project row

   end
      sphinx --> ps: build finished
      ps --> ps: Set build status
      gui --> ps: read build status data
      gui --> gui: Updates project row

   @enduml



Config files
------------
The dompteur configuration files are based on TOML.

The are stored by default in the home directory of the user.

Location for config files is defined via https://github.com/platformdirs/platformdirs

Dompteur config
~~~~~~~~~~~~~~~
:file: dompteur.toml

.. code-block:: toml

   [basic]

   [paths]
   template_folder = "/.."
   projects_folder = "/.."
   default_workspace = "/.."


Project config
~~~~~~~~~~~~~~
:file: {{projects_folder}}/project_x.toml

Used to describe the configuration options of an imported project.
It contains mostly paths and dompteur related information like build commands.

Sphinx config options are not stored and kept inside ``conf.py`` only.

.. code-block:: toml

   name = "Test  project"
   work_dir = "/home/me/workspace/project"

   [builds]

       [builds.html]
       source_dir = "."  # relative workdir
       build_dir = "_build/html"  # relative workdir
       conf = "conf.py"

       builder = "html"
       parallel = True
       clean = True
       verbose = True
       own_command = "sphinx-build -a -E .b html . _build/html"

       [builds.pdf]
       source_dir = "."  # relative workdir
       build_dir = "_build/html"  # relative workdir
       conf = "conf.py"  # relative workdir

       builder = "simplepdf"
       parallel = True
       clean = True
       verbose = True
       own_command = ""



Template config
~~~~~~~~~~~~~~~
Used to load preconfigured configurations.

Dompteur provides own, basic templates.
But users can provide own ones.


