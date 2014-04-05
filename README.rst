Flask webhook for Github
########################
A very simple github post-receive web hook handler that executes per default a pull uppon receiving. The executed action is configurable per repository.

It will also verify that the POST request originated from github.com.

Gettings started
----------------

Edit ``repos.json`` to configure repositories, each repository must be registered under the form ``GITHUB_USER/REPOSITORY_NAME``.

.. code-block:: json

    {
        "razius/puppet": {
            "path": "/home/puppet",
            "action": [["git", "pull", "origin", "master"], ],
        },
        "d3non/somerandomexample/branch:live": {
	    "path": "/home/exampleapp",
	    "action": [["git", "pull", "origin", "live"],
		["echo", "execute", "some", "commands", "..."] ]
	}
    }

Install dependencies.

.. code-block:: console

    pip install -r requirements.txt

Start the server.

.. code-block:: console

    python index.py 80

Start the server behind a proxy (see: http://flask.pocoo.org/docs/deploying/wsgi-standalone/#proxy-setups)

.. code-block:: console

    USE_PROXYFIX=true python index.py 8080



Go to your repository's settings on `github.com <http://github.com>`_ and register your public URL under ``Service Hooks -> WebHook URLs``.
