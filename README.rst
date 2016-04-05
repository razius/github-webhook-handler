Flask webhook for Github
########################
A very simple github post-receive web hook handler that executes per default a
pull uppon receiving. The executed action is configurable per repository.

It will also verify that the POST request originated from github.com or a
defined GitHub Enterprise server.  Additionally will ensure that it has a valid
signature (only when the ``key`` setting is properly configured).

Gettings started
----------------

Installation Requirements
=========================

Install dependencies found in ``requirements.txt``.

.. code-block:: console

    pip install -r requirements.txt

Repository Configuration
========================

Edit ``repos.json`` to configure repositories, each repository must be
registered under the form ``GITHUB_USER/REPOSITORY_NAME``.

.. code-block:: json

    {
        "razius/puppet": {
            "path": "/home/puppet",
            "key": "MyVerySecretKey",
            "action": [["git", "pull", "origin", "master"]]
        },
        "d3non/somerandomexample/branch:live": {
	    "path": "/home/exampleapp",
            "key": "MyVerySecretKey",
	    "action": [["git", "pull", "origin", "live"],
		["echo", "execute", "some", "commands", "..."]]
	}
    }

Runtime Configuration
=====================

Runtime operation is influenced by a set of environment variables which require
being set to influence operation.  Only REPOS_JSON_PATH is required to be set,
as this is required to know how to act on actions from repositories.  The
remaining variables are optional.  USE_PROXYFIX needs to be set to true if
being used behind a WSGI proxy, and is not required otherwise.  GHE_ADDRESS
needs to be set to the IP address of a GitHub Enterprise instance if that is
the source of webhooks.

Set environment variable for the ``repos.json`` config.

.. code-block:: console

    export REPOS_JSON_PATH=/path/to/repos.json

Start the server.

.. code-block:: console

    python index.py 80

Start the server with root privileges, if required, while preserving existing environment variables.

.. code-block:: console

    sudo -E python index.py 80

Start the server behind a proxy (see:
http://flask.pocoo.org/docs/deploying/wsgi-standalone/#proxy-setups)

.. code-block:: console

    USE_PROXYFIX=true python index.py 8080

Start the server to be used with a GitHub Enterprise instance.

.. code-block:: console

   GHE_ADDRESS=192.0.2.50 python index.py 80


Go to your repository's settings on `github.com <http://github.com>`_ or your
GitHub Enterprise instance and register your public URL under
``Webhooks & services -> Webhooks``.
