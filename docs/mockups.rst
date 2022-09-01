Mockups
=======

.. uml::

    @startuml
    (*) --> "
    {{
    salt
    {
    <b>Dompteur start
        {
            Project A | [Build <&key>] | ^HTML^ | --- | [ Configure <&key> ]
            Project B | [Build <&key>] | ^HTML^ | --- | [ Configure <&key> ]
            Project C | [Build <&key>] | ^HTML^ | --- | [ Configure <&key> ]
        }

        {
            [ Create new project ] | [ Import existing project ]
        }
    }
    }}
    " as select

    select -down-> "
    {{
    salt
    {
    <b>Create new project
    Target folder | "/home/me/project_a/docs "
    Project name | "Project A"
    Project author | "Team a"
    [X] Separate build folder
    Project version | "1.0"
    Sphinx version| ^Sphinx 5.1^
    }
    }}

    " as conf_sphinx

    conf_sphinx -down-> "
    {{
    salt
    {
        {
        <b>Select Extensions
        {Filter: | "sphinx"}
        Available Extensions | .| . | Selected extensions
        {SI
        Sphinx-Needs
        Sphinxcontrib-Plantuml
        **Sphinx-Copybutton**
        Sphinx-Collections
        Sphinx-Simplepdf
        } |  [ add ] | [ remove ] |
        {SI
            Sphinx-Copybutton
            Sphinx-Simplepdf
            .
            .
            .
        }
        }
    {
    <b>Extension information
    Lorem ipsum and so ... lorem ipsum and so ... lorem ipsum and so ...
    lorem ipsum and so ...
    }
    }
    }}
    " as conf_ext

    conf_ext -down-> "
    {{
    salt
    {
    <b>Configure Python Environment
    { ^Create new virtual ENV^ }
    {Folder | "/docs/.venv"}

    The next step will create the Venv, install Sphinx and all selected extensions,
    and finally setups a new Sphinx project.
    }
    }}
    " as conv_venf

    @enduml
