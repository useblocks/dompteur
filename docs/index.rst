Welcome to Dompteur's documentation!
====================================

**Dompteur** is an installation and configuration tool for Sphinx, the documentation generator.

It helps users to have a central place for configuration around all elements of the Sphinx universe:

**Creating**
- Sphinx & extension selection
- Creating a Python virtual environment and installing all dependencies
- Executing ``sphinx-quickstart``

**Configuring**
- Showing ``conf.py`` in editor (allows direct manipulations)
- Showing used conf-vars as gui-elements
- Allow search and usage of possible conf-vars

**Building**

**Deploying**


* Sphinx itself
* Sphinx extensions
* Python virtual environment for Sphinx builds
* VSCode/Pycharm configs for bufilding docs

Ideas
-----

Rough gui layout
~~~~~~~~~~~~~~~~
Based on the layout of the new Qubes Configuration tool

Left sidebar, which shows the current config category (install, extensions, config, venv, shortcuts, ...)



Features
~~~~~~~~
* Can create new projects and maintain existing ones
* New projects shall contain

  * preconfigured sphinx project
  * venv
  * Shortcuts on desktop and wherever for build and open docs
  * Config for vscode/pycharm runners (e.g. .vscode folder)
  * (Updated) .gitignore
  * Github actions config to build docs
  * ReadTheDocs config for easy deployment

* Config window, which knows what config options are available

  * Options are searchable
  * Options can be registered by Extensions
  * There is be preconfigured list of options by dompteur for most important stuff

* Config templates from user home directory
* Know existing sphinx-docs by storing confing in home directory

    * Allow to add existing projects

* Can build docs and open browser/editor/presenter directly

  * Has build history and stores result and duration

Technical stuff
~~~~~~~~~~~~~~~
* python script to extrac tconfig options from docs and store them in dompteur-config file
  (e.g. readthedocs, sphinx-needs)
* dompteur config-file, which can be used reproducible setup on new machines
  (for venv, runners, desktop shortcuts, ...)

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   mockups
   workflows
