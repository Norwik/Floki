.. image:: https://img.shields.io/pypi/v/flook.svg
    :alt: PyPI-Server
    :target: https://pypi.org/project/flook/
.. image:: https://github.com/norwik/flook/actions/workflows/ci.yml/badge.svg
    :alt: Build Status
    :target: https://github.com/norwik/flook/actions/workflows/ci.yml

|

======
Flook
======

A Lightweight and Flexible Ansible Command Line Tool.

To use flook, follow the following steps:

1. Create a python virtual environment or use system wide environment

.. code-block::

    $ python3 -m venv venv
    $ source venv/bin/activate


2. Install flook package with pip.

.. code-block::

    $ pip install flook


3. Get flook command line help

.. code-block::

    $ flook --help


4. Init the config file and the database

.. code-block::

    $ flook config init


5. Add recipe

.. code-block::

    $ flook recipe add <recipe_name> -p <recipe_relative_path>
    $ flook recipe add clivern/nginx -p recipe/nginx


6. Add a host

.. code-block::

    $ flook host add <host_name> -i <host_ip> -p <ssh_port> -u <ssh_username> -s <ssh_key_path>
    $ flook host add example.com -i 127.0.0.1 -p 22 -u root -s /Users/root/.ssh/id_rsa.pem


7. Run a recipe towards a host

.. code-block::

    $ flook recipe run <recipe_name> -h <host_name>
    $ flook recipe run clivern/nginx -h example.com
