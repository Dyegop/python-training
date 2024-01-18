"""
BASIC CONCEPTS:
    -You can think of packages as the directories on a file system and modules as files within
    directories.
    -Packages are organized hierarchically, and packages may themselves contain subpackages, as
    well as regular modules.
    -Any module that contains a __path__ attribute is considered a package.
    -It’s important to keep in mind that all packages are modules, but not all modules are
    packages.
    -Python defines two types of packages, regular packages and namespace packages.

REGULAR PACKAGES:
    -Regular packages are traditional packages as they existed in Python 3.2 and earlier.
    -A regular package is typically implemented as a directory containing an __init__.py file.
    -When a regular package is imported, this __init__.py file is implicitly executed, and the
    objects it defines are bound to names in the package’s namespace.
    -The __init__.py file can contain the same Python code that any other module can contain,
    and Python will add some additional attributes to the module when it is imported.
    -Important concepts about __init__.py:
        -If you add imports clauses of classes and functions to the __init__.py file, they would
        be available as a top level object when people import your package.
        -The code in the __init__.py file is ran when you import the package. Think of it as the
        __init__ method inside a class.
        -Another common practice is to add some basic checks to the __init__.py file in order to
        make sure that the package works as expected.

NAMESPACE PACKAGES:
    -A namespace package is a composite of various portions, where each portion contributes a
    subpackage to the parent package.
    -Portions may reside in different locations on the file system, for example, in zip files,
    on the network, or anywhere else that Python searches during import.
    -Namespace packages do not use an ordinary list for their __path__ attribute. They instead
    use a custom iterable type which will automatically perform a new search for package portions
    on the next import attempt within that package if the path of their parent package (or
    "sys.path" for a top level package) changes.
    -With namespace packages, there is no parent/__init__.py file.

__main__.py:
    -Most commonly, the __main__.py file is used to provide a command-line interface for a
    package.
    -Example:
        Consider the following hypothetical package, “bandclass”:
        bandclass
            ├── __init__.py
            ├── __main__.py
            └── student.py
        _main__.py will be executed when the package itself is invoked directly from the command
        line using the -m flag.
        The command "python3 -m bandclass" will cause the __main__.py inside bandclass to run
"""