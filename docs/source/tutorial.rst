========
Tutorial
========

This tutorial will guide you through the process of creating a new FastAPI project using the `cookiecutter-fastapi-project` template.

Installing the cookiecutter template
------------------------------------
.. _installation:

1. Install the `latest version of Cookiecutter <https://cookiecutter.readthedocs.io/en/latest/installation.html>`_
2. Generate the FastAPI sample project::

    cookiecutter https://github.com/DanielLenz/cookiecutter-fastapi-project.git

   This will


Installing Task (optional)
--------------------------

You can optionally install `Task <https://taskfile.dev/installation/>`_ to run the build tasks. This is a modern alternative
to `Makefile`.

These tasks simplify the workflow when working with the FastAPI app. You can find the tasks in the `Taskfile.yml` file. They are also
a great source of documentation for the project structure and the available commands.


Preparing the FastAPI app
-------------------------



To run the FastAPI app, you can use the following command::

    task run


