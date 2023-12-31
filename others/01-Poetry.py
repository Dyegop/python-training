"""
------ BASICS ------

Poetry is a dependency manager.
Poetry has a configuration file called pyproject.toml, in the following format:

# pyproject.toml

[tool.poetry]
name = "rp-poetry"
version = "0.1.0"
description = ""
authors = ["Philipp <philipp@realpython.com>"]

[tool.poetry.dependencies]
python = "^3.9"

[tool.poetry.dev-dependencies]
pytest = "^5.2"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"




------ COMMANDS ------

poetry self update <version>            - Upgrades Poetry to the last version. If <version> is
                                        given, it upgrades/downgrades Poetry to that version.
poetry new <folder_name>  	 			- Create new project.
poetry add <package_name> 	 			- Add an external package to your project.
poetry add <package_name> -D/--dev 		- Add an external package specifying that it is a dev
                                        dependency.
poetry add `cat requirements.txt`		- Add dependecies to a project from requirements txt file.
poetry --version		  	 			- Print installed version of poetry.
poetry env list			     			- List installed envs in the current directory.
poetry install		         			- Check for dependencies, resolves and install them. A
                                        pyproject.toml is required.
poetry lock                             - Reads the pyproject.toml file from the current
                                        directory, processes it, and locks the dependencies in
                                        the poetry.lock file.
poetry update							-> Update all dependencies
poetry update <dependency_name>			-> Update a given dependecy or dependecies.
poetry export --output requirements.txt -> Export poetry dependecies to a requirements file.
poetry env use "path/to/python.exe"     -> Use env for the python version in the given path the
                                        path must be added with quotation marks.




------ CONFIGURATION ------

The pyproject.toml file is divided in sections called tables. 
They contain instructions that tools like Poetry recognize and use for dependency management or
build routines.
If a table name is tool-specific, it must be prefixed with tool keyword. 
By using such a subtable, you can add instructions for different tools in your project.

Subtables:
    [tool.poetry] -> general information
                  -> Available keys are defined by Poetry
                  -> Some keys are optional, but there are four that you must specify:
                        -name: the name of your package
                        -version: the version of your package, ideally following semantic
                        versioning
                        -description: a short description of your package
                        -authors: a list of authors, in the format name <email>
    [tool.poetry.dependencies] -> project required libraries
    [tool.poetry.dev-dependencies] -> libraries required by developers order to build and program
    the project, but which should not be used in production
    [build-system] ->

Poetry has lock file (poetry.lock) that prevents you from automatically getting the latest
versions of your dependencies.
"""
