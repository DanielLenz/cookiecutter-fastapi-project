############################
Cookiecutter FastAPI project
############################

Cookiecutter template for a FastAPI app.

* GitHub repo: https://github.com/DanielLenz/cookiecutter-fastapi-project
* Documentation: https://cookiecutter-fastapi-project.readthedocs.io
* Free software: BSD-3 license


Quickstart
----------

1. Install the `latest version of Cookiecutter <https://cookiecutter.readthedocs.io/en/latest/installation.html>`_
2. Generate the FastAPI sample project::

    cookiecutter https://github.com/DanielLenz/cookiecutter-fastapi-project.git

3. Optionally, `install Task <https://taskfile.dev/installation/>`_ to run the build tasks.
4. Follow the tasks in `Taskfile.yml` to run the FastAPI app
    

Features
--------

.. _features:

- `Taskfile <https://taskfile.dev/>`_ as a modern alternative to `Makefile` to perform e.g. the common build tasks
- Test suite, including mocking DB connections following `best practices <https://fastapi.tiangolo.com/advanced/testing-database/>`_
- `A simple Dockerfile <https://fastapi.tiangolo.com/deployment/docker/#dockerfile>`_ to run the FastAPI app in a container
- Various examples for `middleware <https://fastapi.tiangolo.com/advanced/middleware/>`_, including HTTPS redirection, CORS, and rate limiting
- Proper project setup following `the official FastAPI documentation <https://fastapi.tiangolo.com/tutorial/bigger-applications/>`_

Coming soon
-----------

Some of the features that I'd like to add in the near future are

- GitHub Actions for basic CI/CD setup
- Proper logging setup
- Examples for websocket connections
- A basic security setup
