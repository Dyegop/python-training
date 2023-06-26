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

poetry new <folder_name>  	 			-> create new project.
poetry add <package_name> 	 			-> add an external package to your project.
poetry add <package_name> -D/--dev 		-> add an external package specifying that it is a dev
                                        dependency.
poetry add `cat requirements.txt`		-> add dependecies to a project from requirements txt file
poetry --version		  	 			-> print installed version of poetry.
poetry env list			     			-> list installed envs in the current directory.
poetry install		         			-> check for dependencies, resolves and install them. A
                                        pyproject.toml is required.
poetry update							-> update all dependencies
poetry update <dependency_name>			-> update a given dependecy or dependecies (e.g, poetry
                                        update requests beautifulsoup4).
poetry export --output requirements.txt -> export poetry dependecies to a requirements file.
poetry env use "path/to/python.exe"     -> use env for the python version in the given path
                                        -> the path must be added with quotation marks




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
