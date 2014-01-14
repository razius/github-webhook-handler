Flask Github webhook
####################
A very simple github post-receive web hook handler that executes a pull uppon receiving.

It will also verify that the POST request originated from github.com.


Edit `repos.json` to configure repositories, each repository must be registered under the form `GITHUB_USER/REPOSITORY_NAME`.

.. code-block:: json

    {
        "razius/puppet": {
            "path": "/home/puppet"
        }
    }

Start the server.

.. code-block:: console

    python index.py 80

Go to your repository's settings on `github.com`_ and register your public URL under `Service Hooks -> WebHook URLs`.
